from vmcjp.slack.messages import message_handler

def command_handler(cmd, event, db):
    eval(cmd)(event, db)

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
            "command": "register org",
        }
    )

def delete_org(event, db):
    message_handler(constant.DELETE_ORG, event)
    db.delete_cred_db(event["user_id"])
