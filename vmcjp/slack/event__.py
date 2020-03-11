from vmcjp.utils.loginutils import validate_token
from vmcjp.utils import dbutils
from vmcjp.utils import constant
from vmcjp.slack.messages import message_handler
from vmcjp.vmc.vmc_client import get_vmc_client, list_sddcs, get_max_num_hosts, is_network, is_valid_network

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
                message_handler(constant.MAX_HOSTS, event)
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
                message_handler(constant.RESTORE_WIZARD, event)
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
                message_handler(constant.RESTORE, event)
        elif "list sddcs" in text:
            if __cred_data is None:
                message_handler(constant.ASK_REGISTER_TOKEN, event)
            elif "registered" in __cred_data.get("status"):
                event_cred_update(event, __cred_data)
                vmc_client = get_vmc_client(event.get("token"))
                sddcs = vmc_client.orgs.Sddcs.list(event.get("org_id"))
                message_handler(constant.SDDCS_TXT, event)
                for sddc in sddcs:
                    event.update(
                        {
                            "sddc_name": sddc.name,
                            "user_name": sddc.user_name,
                            "created": sddc.created.isoformat(),
                            "num_hosts": len(sddc.resource_config.esx_hosts)
                        }
                    )
                    message_handler(constant.SDDCS_MSG, event)
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
                    message_handler(constant.SDDC_CONFIRM, event)
                    db.write_event_db(
                        event.get("user_id"), 
                        {
                            "status": "vpc_cidr", 
                            "vpc_cidr": event.get("text")
                        }
                    )
                else:
                    message_handler(constant.WRONG_NETWORK, event)
            return
        else:
            if result.get("status") == "region":
                if result.get("max_hosts") == 1:
                    message_handler(constant.LINK_AWS, event)
                else:
                    message_handler(constant.SINGLE_MULTI, event)
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
            message_handler(constant.CANCEL_RESTORE, event)
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
                    "org_id": event.get("text")
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
