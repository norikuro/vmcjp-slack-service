from vmcjp.slack.messages import message_handler

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
