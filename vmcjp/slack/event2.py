from vmcjp.utils import dbutils
from vmcjp.utils import constant
from vmcjp.slack.messages import message_handler

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
            eval(constant.COMMAND_ORG[text])(event)
            return
        elif text in constant.COMMAND_SDDC:
            if cred is not None:
                eval(constant.COMMAND_SDDC[text])(event)
                return
            else:
                message_handler(constant.ASK_REGISTER_TOKEN, event)
                return
