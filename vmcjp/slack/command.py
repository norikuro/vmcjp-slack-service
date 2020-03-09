from vmcjp.utils import constant
from vmcjp.utils.loginutils import validate_token
from vmcjp.slack.messages import message_handler
from vmcjp.vmc.vmc_client import list_sddcs_, get_max_num_hosts, list_sddcs

def command_handler(cmd, event, db):
    eval(cmd)(event, db)

#def help(event):
#    message_handler(constant.HELP, event)

def cancel(event, db):
    message_handler(constant.CANCEL_TOKEN, event)
    db.delete_cred_db(event.get("user_id"))

def register_org(event, db):
    message_handler(constant.REGISTER_ORG, event)
    db.write_cred_db(
        event.get("user_id"), 
        {
            "status": "registering",
            "org_id": event.get("text")
        }
    )

def register_token(event, db):
    user_name = validate_token(event.get("text"), cred.get("org_id"))
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
    else:
        message_handler(constant.FAILED_TOKEN, event)
        message_handler(constant.WRONG_TOKEN, event)
        db.delete_cred_db(event.get("user_id"))

def delete_org(event, db):
    message_handler(constant.DELETE_ORG, event)
    db.delete_cred_db(event.get("user_id"))

def list_sddcs(event, db):
    message_handler(constant.SDDCS_TXT, event)
    event.update(
        {
            "sddcs": list_sddcs_(
                event.get("token"), 
                event.get("org_id")
            )
        }
    )
#    vmc_client = get_vmc_client(event.get("token"))
#    sddcs = vmc_client.orgs.Sddcs.list(event.get("org_id"))
#    for sddc in sddcs:
#        event.update(
#            {
#                "sddc_name": sddc.name,
#                "user_name": sddc.user_name,
#                "created": sddc.created.isoformat(),
#                "num_hosts": len(sddc.resource_config.esx_hosts)
#            }
#        )
#        message_handler(constant.SDDCS_MSG, event)
    message_handler(constant.SDDCS_MSG, event)

def create_sddc(event, db):
    message_handler(constant.SDDC_WIZARD, event)
    message_handler(constant.CHECK_RESOURCE, event)
    max_hosts = get_max_num_hosts(
        event.get("token"),
        event.get("org_id")
    )
    event.update({"max_hosts": max_hosts})
    if max_hosts < 1:
        message_handler(constant.NOT_ENOUGH, event)
        db.delete_event_db(event.get("user_id"))
    else:
        message_handler(constant.MAX_HOSTS, event)
        db.write_event_db(
            event.get("user_id"), 
            {
                "command": constant.COMMAND_SDDC[event.get(text)],
                "status": constant.CHECK_MAX_HOSTS, 
                "max_hosts": max_hosts,
                "provider": "AWS"
            }
        )

def delete_sddc(event, db):
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
            "command": constant.COMMAND_SDDC[event.get(text)],
            "status": constant.DELETE_SDDC
        }
    )
