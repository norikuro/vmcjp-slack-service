from vmcjp.slack.messages import message_handler

def command_handler(cmd, event, db=None):
    if db is None:
        eval(cmd)(event)
    elif db is not None:
        eval(cmd)(event, db)

def help(event):
    message_handler(constant.HELP, event)

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
