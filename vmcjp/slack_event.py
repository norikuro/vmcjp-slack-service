import json
import logging
import ipaddress
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.slack_post import post_text, post_button, post_option, post_field_button
from vmcjp.utils.lambdautils import call_lambda
from vmcjp.utils.vmc import validate_token
from vmcjp.utils import dbutils2
from vmcjp.utils import constant
from vmcjp import slack_message

PRECHECK_BUTTON = constant.BUTTON_DIR + "precheck.json"
LINK_AWS_BUTTON = constant.BUTTON_DIR + "link_aws.json"
SINGLE_MULTI_BUTTON = constant.BUTTON_DIR + "single_multi.json"
CREATE_BUTTON = constant.BUTTON_DIR + "create.json"
HELP_BUTTON = constant.BUTTON_DIR + "help.json"
LIST_BUTTON = constant.BUTTON_DIR + "list.json"
DELETE_BUTTON = constant.BUTTON_DIR + "delete.json"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_max_num_hosts(token, org_id):
# get deployable number of hosts
# 1 host is for Storage EDRS
    
    vmc_client = get_vmc_client(token)
    
    sddcs = vmc_client.orgs.Sddcs.list(org_id)
#    sddcs = vmc_client.orgs.Sddcs.list(TEST_ORG_ID) #for test 
    
    i = 0
    for sddc in sddcs:
        i += len(sddc.resource_config.esx_hosts)
    max_hosts = (int(vmc_client.Orgs.get(org_id).properties.values["sddcLimit"]) - 1) - i
#    if max_hosts < 1:
#        return max_hosts
#    else:
#        return 1 if max_hosts < 3 else max_hosts
    return 4 #for test

def get_vmc_client(token):
    session = requests.Session()
    vmc_client = create_vmc_client(token, session=session)
    atexit.register(session.close)
    return vmc_client

def is_network(address):
    try:
        ipaddress.ip_network(address)
        return True
    except ValueError:
        return False

def is_valid_token(event):
    try:
        get_vmc_client(event.get("text")).orgs.Sddcs.list(event.get("org_id"))
        return True
    except KeyError:
        return False

def is_valid_network(address):
    try:
        nw = ipaddress.ip_network(address)
    except ValueError:
        return False
    
    prefix = nw.prefixlen
    if prefix != 23 and prefix != 20 and prefix != 16:
        return False
    
    rs10 = ipaddress.ip_network(u'10.0.0.0/15')
    rs192 = ipaddress.ip_network(u'192.168.1.0/24')
    rs172 = ipaddress.ip_network(u'172.31.0.0/16')

    if nw.subnet_of(rs10):
        return False
    elif rs192.subnet_of(nw):
        return False
    elif nw.subnet_of(rs172):
        return False
    
    nw10 = ipaddress.ip_network(u'10.0.0.0/8')
    nw172 = ipaddress.ip_network(u'172.16.0.0/12')
    nw192 = ipaddress.ip_network(u'192.168.0.0/16')
    
    if nw.subnet_of(nw10):
        return True
    elif nw.subnet_of(nw172):
        return True
    elif nw.subnet_of(nw192):
        return True
    else:
        return False

def list_sddcs(vmc_client, token, org_id):
    vmc_client = get_vmc_client(token)
    sddcs = vmc_client.orgs.Sddcs.list(org_id)
    return [
        {
            "text": sddc.name,
            "value": "{}+{}".format(sddc.name, sddc.id)
        } for sddc in sddcs
    ]

def event_handler(event):
    text = event.get("text").lower()
    
    db = dbutils2.DocmentDb(event.get("db_url"))
    current = db.read_event_db(event.get("user_id"), 120)
    if current is not None and current.get("status") == "creating":
        slack_message.ask_wait_to_finish_task_message(event)
        return
    
    result = db.read_event_db(event.get("user_id"), 5)
    __cred_data = db.read_cred_db(event.get("user_id"))
    if result is None:
        if "create sddc" in text:
            if __cred_data is None:
                slack_message.ask_register_token_message(event)
            elif "registered" in __cred_data.get("status"):
                event.update({"token": __cred_data.get("token")})
                slack_message.start_create_sddc_wizard_message(event)
                event.update(
                    {
                        "max_hosts": get_max_num_hosts(
                            event.get("token"), 
                            event.get("org_id")
                        )
                    }
                )
                if event.get("max_hosts") < 1:
                    slack_message.no_enough_resouces_message(event)
                    db.delete_event_db(event.get("user_id"))
                    return
                slack_message.max_hosts_message(event)
                db.write_event_db(
                    event.get("user_id"), 
                    {
                        "command": "create",
                        "status": "create_sddc", 
                        "max_hosts": event.get("max_hosts")
                    }
                )
            return
        elif "delete sddc" in text:
            if __cred_data is None:
                slack_message.ask_register_token_message(event)
            elif "registered" in __cred_data.get("status"):
                event.update({"token": __cred_data.get("token")})
                event.update(
                    {
                        "option_list": list_sddcs(
                            get_vmc_client(event.get("token")), 
                            event.get("token"), 
                            event.get("org_id")
                        )
                    }
                )
                slack_message.delete_sddc_message(event)
                db.write_event_db(
                    event.get("user_id"), 
                    {
                        "command": "delete", 
                        "status": "delete_sddc"
                    }
                )
        elif "restore sddc" in text: #for internal use
            if __cred_data is None:
                slack_message.ask_register_token_message(event)
            elif "registered" in __cred_data.get("status"):
                event.update({"token": __cred_data.get("token")})
                call_lambda("restore_sddc", event)
                db.write_event_db(
                    event.get("user_id"), 
                    {
                        "command": "restore", 
                        "status": "restore_sddc"
                    }
                )
        elif "list sddcs" in text:
            if __cred_data is None:
                slack_message.ask_register_token_message(event)
            elif "registered" in __cred_data.get("status"):
                event.update({"token": __cred_data.get("token")})
                vmc_client = get_vmc_client(event.get("token"))
                sddcs = vmc_client.orgs.Sddcs.list(event.get("org_id"))
                slack_message.list_sddcs_text_message(event)
#                response = post_text(
#                    event,
#                    "Here is SDDCs list in this org.",
#                    "bot"
#                )
#                logging.info(response.read())
                for sddc in sddcs:
                    event.update(
                        {
                            "sddc_name": sddc.name,
                            "user_name": sddc.user_name,
                            "created": sddc.created.isoformat(),
                            "num_hosts": len(sddc.resource_config.esx_hosts)
                        }
                    )
                    slack_message.list_sddcs_message(event)
#                    response = post_field_button(
#                        event, 
#                        LIST_BUTTON, 
#                        type="bot"
#                    )
#                    logging.info(response.read())
            return
        elif "register token" in text:
            response = post_text(
                event,
                "Please enter VMC refresh token.",
                "bot"
            )
#            logging.info(response.read())
            db.write_cred_db(
                event.get("user_id"), 
                {
                    "status": "registering"
                }
            )
            db.write_event_db(
                event.get("user_id"), 
                {
                    "command": "register",
                    "status": "registering"
                }
            )
            return
        elif "delete token" in text:
            response = post_text(
                event,
                "Deleted VMC refresh token from system db.",
                "bot"
            )
#            logging.info(response.read())
            db.delete_cred_db(event["user_id"])
            return
        elif "help" in text:
            response = post_button(event, HELP_BUTTON, "bot")
#            logging.info(response.read())
            return
        elif "cancel" in text:
            if __cred_data is not None and "registering" in __cred_data.get("status"):
                response = post_text(
                    event,
                    "Canceled to register VMC refresh token.",
                    "bot"
                )
#                logging.info(response.read())
                db.delete_cred_db(event.get("user_id"))
            else:
                response = post_text(event, constant.HELP, "bot")
            return
        else:
            response = post_text(event, constant.HELP, "bot")
#            logging.info(response.read())
            return
    elif "create" in result.get("command"):
        if "create sddc" in text:
            return
        elif "cancel" in text:
            response = post_text(
                event,
                "OK, canceled a create sddc wizard.",
                "bot"
            )
#            logging.info(response.read())
            db.delete_event_db(event.get("user_id"))
            return
        elif text.find(" ") != -1:
            return
        elif is_network(text):
            if result.get("status") == "link_aws" or "subnet":
                if is_valid_network(text):
                    event.update(
                        {"vpc_cidr": event.get("text")}
                    )
                    event.update(result)
                    post_field_button(
                        event, 
                        CREATE_BUTTON, 
                        type="bot"
                    )
                    db.write_event_db(
                        event.get("user_id"), 
                        {
                            "status": "vpc_cidr", 
                            "vpc_cidr": event.get("text")
                        }
                    )
                else:
                    response = post_text(
                        event,
                        "Please enter correct network cidr block.",
                        "bot"
                    )
            return
        else:
            if result.get("status") == "region":
                if result.get("max_hosts") == 1:
                    response = post_button(event, LINK_AWS_BUTTON, "bot")
#                    logging.info(response.read())
                else:
                    response = post_button(event, SINGLE_MULTI_BUTTON, "bot")
#                    logging.info(response.read())
                db.write_event_db(
                    event.get("user_id"), 
                    {
                        "status": "sddc_name", 
                        "sddc_name": event.get("text")
                    }
                )
            return
    elif "register" in result.get("command"):
        if "cancel" in text:
            response = post_text(
                event,
                "OK, token registration has canceled",
                "bot"
            )
#            logging.info(response.read())
            db.delete_event_db(event.get("user_id"))
            db.delete_cred_db(event.get("user_id"))
        else:
            user_name = validate_token(event.get("text"))
            if user_name is not None:
                response = post_text(
                    event,
                    "Registered VMC refresh token to system db, you can delete it with `delete token`.",
                    "bot"
                )
#                logging.info(response.read())
                db.write_cred_db(
                    event.get("user_id"), 
                    {
                        "status": "registered", 
                        "token": event.get("text"), 
                        "user_name": user_name
                    }
                )
                db.delete_event_db(event["user_id"])
            else:
                response = post_text(
                    event,
                    "Token number you entered is something wrong, please check your token and enter correct token.",
                    "bot"
                )
#                logging.info(response.read())
