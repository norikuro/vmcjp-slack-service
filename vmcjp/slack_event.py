import json
import logging
import ipaddress
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client
#from vmcjp.utils.lambdautils import call_lambda
from vmcjp.utils.vmc import validate_token
from vmcjp.utils import dbutils
from vmcjp.utils import constant
from vmcjp import slack_message

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_max_num_hosts(token, org_id):
# get deployable number of hosts
# 1 host is for Storage EDRS
    
    vmc_client = get_vmc_client(token)
    
    sddcs = vmc_client.orgs.Sddcs.list(org_id)
    
    i = 0
    for sddc in sddcs:
        i += len(sddc.resource_config.esx_hosts)
    max_hosts = (int(vmc_client.Orgs.get(org_id).properties.values["sddcLimit"]) - 1) - i
#    if max_hosts < 1:
#        return max_hosts
#    else:
#        return 1 if max_hosts < 3 else max_hosts
    return 4 #for test

def get_max_num_hosts_zerocloud(token, org_id): #for internal use
    vmc_client = get_vmc_client(token)
    return int(vmc_client.Orgs.get(org_id).properties.values["maxHostsPerSddcOnCreate"])

def get_vmc_client(token):
    session = requests.Session()
    vmc_client = create_vmc_client(token, session=session)
    atexit.register(session.close)
    return vmc_client

def list_region(vmc_client, org_id):
    regions = vmc_client.Orgs.get(org_id).properties.values.get("defaultAwsRegions").split(",")
    return [
        {
            "text": region,
            "value": region
        } for region in regions
    ]

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

def event_cred_update(event, cred):
    event.update(
        {
            "token": cred.get("token"),
            "org_id": cred.get("org_id")
        }
    )
#    logging.info(event)

def event_handler(event):
    text = event.get("text").lower()

    db = dbutils.DocmentDb(event.get("db_url"))
    current = db.read_event_db(event.get("user_id"), 120)
    if current is not None and current.get("status") == "creating":
        slack_message.ask_wait_to_finish_task_message(event)
        return
    
    result = db.read_event_db(event.get("user_id"), 5)
    __cred_data = db.read_cred_db(event.get("user_id"))
    if result is None:
        if "create sddc on zerocloud" in text: #for internal use only
            if __cred_data is None:
                slack_message.ask_register_token_message(event)
            elif "registered" in __cred_data.get("status"):
                event_cred_update(event, __cred_data)
                slack_message.start_create_sddc_wizard_message(event)
                slack_message.check_resources_message(event)
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
                        "max_hosts": event.get("max_hosts"),
                        "provider": "ZEROCLOUD"
                    }
                )
            return
        elif "create sddc" in text:
            if __cred_data is None:
                slack_message.ask_register_token_message(event)
            elif "registered" in __cred_data.get("status"):
                event_cred_update(event, __cred_data)
                slack_message.start_create_sddc_wizard_message(event)
                slack_message.check_resources_message(event)
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
                        "max_hosts": event.get("max_hosts"),
                        "provider": "AWS"
                    }
                )
            return
        elif "delete sddc" in text:
            if __cred_data is None:
                slack_message.ask_register_token_message(event)
            elif "registered" in __cred_data.get("status"):
                event_cred_update(event, __cred_data)
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
                slack_message.start_restore_wizard_message(event)
                config = db.get_backedup_sddc_config()
                event.update(config)
                event_cred_update(event, __cred_data)
                config.update(
                    {
                        "command": "restore", 
                        "status": "restore_sddc"
                    }
                )
                db.write_event_db(event.get("user_id"), config)
                slack_message.restore_message(event)
        elif "list sddcs" in text:
            if __cred_data is None:
                slack_message.ask_register_token_message(event)
            elif "registered" in __cred_data.get("status"):
                event_cred_update(event, __cred_data)
#                event.update(
#                    {
#                        "token": __cred_data.get("token")#,
#                        "org_id": __cred_data.get("org_id")
#                    }
#                )
                vmc_client = get_vmc_client(event.get("token"))
                sddcs = vmc_client.orgs.Sddcs.list(event.get("org_id"))
                slack_message.list_sddcs_text_message(event)
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
            return
#        elif "register token" in text:
#            slack_message.register_token_message(event)
#            db.write_cred_db(
#                event.get("user_id"), 
#                {
#                    "status": "registering"
#                }
#            )
#            db.write_event_db(
#                event.get("user_id"), 
#                {
#                    "command": "register token",
#                    "status": "registering"
#                }
#            )
#            return
        elif "register org" in text:
            slack_message.register_org_message(event)
            db.write_cred_db(
                event.get("user_id"), 
                {
                    "status": "registering"
                }
            )
            db.write_event_db(
                event.get("user_id"), 
                {
                    "command": "register org",
                    "status": "registering org"
                }
            )
            return
        elif "delete org" in text:
            slack_message.delete_org_message(event)
            db.delete_cred_db(event["user_id"])
            return
        elif "help" in text:
            slack_message.help_message(event)
            return
        elif "cancel" in text:
            if __cred_data is not None and "registering" in __cred_data.get("status"):
                slack_message.cancel_token_registration_message(event)
                db.delete_cred_db(event.get("user_id"))
            else:
                slack_message.may_i_message(event)
            return
        else:
            slack_message.may_i_message(event)
            return
    elif "create" in result.get("command"):
        if "create sddc" in text:
            return
        elif "cancel" in text:
            slack_message.cancel_sddc_creation_message(event)
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
                    slack_message.create_sddc_confirmation_message(event)
                    db.write_event_db(
                        event.get("user_id"), 
                        {
                            "status": "vpc_cidr", 
                            "vpc_cidr": event.get("text")
                        }
                    )
                else:
                    slack_message.wrong_network_message(event)
            return
        else:
            if result.get("status") == "region":
                if result.get("max_hosts") == 1:
                    slack_message.link_aws_message(event)
                else:
                    slack_message.single_multi_message(event)
                db.write_event_db(
                    event.get("user_id"), 
                    {
                        "status": "sddc_name", 
                        "sddc_name": event.get("text")
                    }
                )
            elif result.get("status") in constant.INT_STATUS:
                slack_message.ask_select_button_message(event)
            return
    elif "delete" in result.get("command"):
        if "cancel" in text:
            slack_message.cancel_sddc_deletion_message(event)
            db.delete_event_db(event.get("user_id"))
    elif "restore" in result.get("command"):
        if "cancel" in text:
            slack_message.cancel_sddc_restoration_message(event)
            db.delete_event_db(event.get("user_id"))
#    elif "register token" in result.get("command"):
#        if "cancel" in text:
#            slack_message.cancel_token_registration_message(event)
#            db.delete_event_db(event.get("user_id"))
#            db.delete_cred_db(event.get("user_id"))
#        else:
#            user_name = validate_token(event.get("text"))
#            if user_name is not None:
#                slack_message.succeed_token_registratuin_message(event)
#                db.write_cred_db(
#                    event.get("user_id"), 
#                    {
#                        "status": "registered", 
#                        "token": event.get("text"), 
#                        "user_name": user_name
#                    }
#                )
#                db.delete_event_db(event["user_id"])
#            else:
#                slack_message.wrong_token_message(event)
    elif "register org" in result.get("command"):
        if "cancel" in text:
            slack_message.cancel_org_registration_message(event)
            db.delete_event_db(event.get("user_id"))
            db.delete_cred_db(event.get("user_id"))
        elif "registering org" in result.get("status"):
            slack_message.succeed_org_registratuin_message(event)
            db.write_cred_db(
                event.get("user_id"), 
                {
#                    "status": "registered", 
#                    "org_id": event.get("text"), 
                    "org_id": event.get("text")
#                    "user_name": user_name
                }
            )
            db.write_event_db(
                event.get("user_id"), 
                {
                    "status": "registering token"
                }
            )
            slack_message.register_token_message(event)
        elif "registering token" in result.get("status"):
            try:
                user_name = validate_token(event.get("text"), __cred_data.get("org_id"))
            except Exception as e:
                event.update({"message": e.message})
                slack_message.failed_token_registratuin_message(event)
            if user_name is not None:
                slack_message.succeed_token_registratuin_message(event)
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
                slack_message.wrong_token_message(event)
