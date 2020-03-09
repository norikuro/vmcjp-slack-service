from vmcjp.utils import dbutils
from vmcjp.utils import constant
from vmcjp.slack.messages import message_handler
from vmcjp.slack.command import command_handler

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
    
    event_db = db.read_event_db(event.get("user_id"), 5)
    cred = db.read_cred_db(event.get("user_id"))
    if event_db is None:
        if text in constant.COMMAND_ORG:
            command_handler(constant.COMMAND_ORG[text], event, db)
            return
        elif text in constant.COMMAND_SDDC:
            if cred is not None and "registered" in cred.get("status"):
                event_cred_update(event, cred)
                command_handler(constant.COMMAND_SDDC[text], event, db)
                return
            else:
                message_handler(constant.ASK_REGISTER_TOKEN, event)
                return
        elif text == "help":
            message_handler(constant.HELP, event)
        else:
            message_handler(constant.MAY_I, event)
            return
