from vmcjp.slack.messages import message_handler
from vmcjp.vmc.vmc_client import list_sddcs_, get_max_num_hosts, 

def command_handler(cmd, event, db=None):
    if db is None:
        eval(cmd)(event)
    elif db is not None:
        eval(cmd)(event, db)

def help(event):
    message_handler(constant.HELP, event)

def cancel(event, db):
    message_handler(constant.CANCEL_TOKEN, event)
    db.delete_cred_db(event.get("user_id"))

def register_org(event, db):
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
            "command": "register_org",
        }
    )

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
                "command": "create_sddc",
                "status": constant.CHECK_MAX_HOSTS, 
                "max_hosts": max_hosts,
                "provider": "AWS"
            }
