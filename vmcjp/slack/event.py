import logging
import ipaddress
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.vmc import validate_token
from vmcjp.utils import dbutils
from vmcjp.utils import constant
from vmcjp.slack.message.messages import message_handler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_vmc_client(token):
    session = requests.Session()
    vmc_client = create_vmc_client(token, session=session)
    atexit.register(session.close)
    return vmc_client

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

#def get_max_num_hosts_zerocloud(token, org_id): #for internal use
#    vmc_client = get_vmc_client(token)
#    return int(vmc_client.Orgs.get(org_id).properties.values["maxHostsPerSddcOnCreate"])

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

def list_sddcs(token, org_id):
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

def event_handler(event):
    text = event.get("text").lower()

    db = dbutils.DocmentDb(event.get("db_url"))
    current = db.read_event_db(event.get("user_id"), 120)
    if current is not None and current.get("status") == "creating":
        message_handler(constant.ASK_WAIT_TASK, event)
        return
    
    result = db.read_event_db(event.get("user_id"), 5)
    __cred_data = db.read_cred_db(event.get("user_id"))
    if result is None:
        if "create sddc on zerocloud" in text: #for internal use only
            if __cred_data is None:
                message_handler(constant.ASK_REGISTER_TOKEN, event)
            elif "registered" in __cred_data.get("status"):
                event_cred_update(event, __cred_data)
                message_handler(constant.SDDC_WIZARD, event)
                message_handler(constant.CHECK_RESOURCE, event)
                event.update(
                    {
                        "max_hosts": get_max_num_hosts(
                            event.get("token"), 
                            event.get("org_id")
                        )
                    }
                )
                if event.get("max_hosts") < 1:
                    message_handler(constant.NOT_ENOUGH, event)
                    db.delete_event_db(event.get("user_id"))
                    return
                message_handler(constant.MAX_HOSTS, event)
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
                message_handler(constant.ASK_REGISTER_TOKEN, event)
            elif "registered" in __cred_data.get("status"):
                event_cred_update(event, __cred_data)
                message_handler(constant.SDDC_WIZARD, event)
                message_handler(constant.CHECK_RESOURCE, event)
                event.update(
                    {
                        "max_hosts": get_max_num_hosts(
                            event.get("token"), 
                            event.get("org_id")
                        )
                    }
                )
                if event.get("max_hosts") < 1:
                    message_handler(constant.NOT_ENOUGH, event)
                    db.delete_event_db(event.get("user_id"))
                    return
                messages.max_hosts_message(event)
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
                message_handler(constant.ASK_REGISTER_TOKEN, event)
            elif "registered" in __cred_data.get("status"):
                event_cred_update(event, __cred_data)
                event.update(
                    {
                        "option_list": list_sddcs(
                            event.get("token"), 
                            event.get("org_id")
                        )
                    }
                )
                message_handler(constant.DELETE_SDDC, event)
                db.write_event_db(
                    event.get("user_id"), 
                    {
                        "command": "delete", 
                        "status": "delete_sddc"
                    }
                )
        elif "restore sddc" in text: #for internal use
            if __cred_data is None:
                message_handler(constant.ASK_REGISTER_TOKEN, event)
            elif "registered" in __cred_data.get("status"):
                messages.start_restore_wizard_message(event)
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
                messages.restore_message(event)
        elif "list sddcs" in text:
            if __cred_data is None:
                message_handler(constant.ASK_REGISTER_TOKEN, event)
            elif "registered" in __cred_data.get("status"):
                event_cred_update(event, __cred_data)
                vmc_client = get_vmc_client(event.get("token"))
                sddcs = vmc_client.orgs.Sddcs.list(event.get("org_id"))
                messages.list_sddcs_text_message(event)
                for sddc in sddcs:
                    event.update(
                        {
                            "sddc_name": sddc.name,
                            "user_name": sddc.user_name,
                            "created": sddc.created.isoformat(),
                            "num_hosts": len(sddc.resource_config.esx_hosts)
                        }
                    )
                    messages.list_sddcs_message(event)
            return

        elif "register org" in text:
            message_handler(constant.REGISTER_ORG, event)
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
            message_handler(constant.DELETE_ORG, event)
            db.delete_cred_db(event["user_id"])
            return
        elif "help" in text:
            message_handler(constant.HELP, event)
            return
        elif "cancel" in text:
            if __cred_data is not None and "registering" in __cred_data.get("status"):
                message_handler(constant.CANCEL_TOKEN, event)
                db.delete_cred_db(event.get("user_id"))
            else:
                message_handler(constant.MAY_I, event)
            return
        else:
            message_handler(constant.MAY_I, event)
            return
    elif "create" in result.get("command"):
        if "create sddc" in text:
            return
        elif "cancel" in text:
            message_handler(constant.CANCEL_SDDC, event)
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
                    messages.create_sddc_confirmation_message(event)
                    db.write_event_db(
                        event.get("user_id"), 
                        {
                            "status": "vpc_cidr", 
                            "vpc_cidr": event.get("text")
                        }
                    )
                else:
                    messages.wrong_network_message(event)
            return
        else:
            if result.get("status") == "region":
                if result.get("max_hosts") == 1:
                    messages.link_aws_message(event)
                else:
                    messages.single_multi_message(event)
                db.write_event_db(
                    event.get("user_id"), 
                    {
                        "status": "sddc_name", 
                        "sddc_name": event.get("text")
                    }
                )
            elif result.get("status") in constant.INT_STATUS:
                message_handler(constant.ASK_SELECT_BUTTON, event)
            return
    elif "delete" in result.get("command"):
        if "cancel" in text:
            message_handler(constant.CANCEL_DELETE, event)
            db.delete_event_db(event.get("user_id"))
    elif "restore" in result.get("command"):
        if "cancel" in text:
            messages.cancel_sddc_restoration_message(event)
            db.delete_event_db(event.get("user_id"))
    elif "register org" in result.get("command"):
        if "cancel" in text:
            message_handler(constant.CANCEL_ORG, event)
            db.delete_event_db(event.get("user_id"))
            db.delete_cred_db(event.get("user_id"))
        elif "registering org" in result.get("status"):
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
            message_handler(constant.REGISTER_TOKEN, event)
        elif "registering token" in result.get("status"):
                user_name = validate_token(event.get("text"), __cred_data.get("org_id"))
                if user_name is not None:
                    message_handler(constant.SUCCESS_TOKEN, event)
                    db.write_cred_db(
                        event.get("user_id"), 
                        {
                            "status": "registered", 
                            "token": event.get("text"), 
                            "user_name": user_name
                        }
                    )
                    db.delete_event_db(event.get("user_id"))
                else:
                    message_handler(constant.FAILED_TOKEN, event)
                    message_handler(constant.WRONG_TOKEN, event)
                    db.delete_event_db(event.get("user_id"))
                    db.delete_cred_db(event.get("user_id"))
