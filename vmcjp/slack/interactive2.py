from vmcjp.utils import dbutils
from vmcjp.slack.messages import message_handler
from vmcjp.slack.command import command_handler

def interactive_handler(event):
    user_id = event.get("user_id")
    
    db = dbutils.DocmentDb(event.get("db_url"))
    event_db = db.read_event_db(user_id, 5)
    
    if event_db is None:
      message_handler(constant.MAY_I, event)
      return
    
    cred_db = db.read_cred_db(event.get("user_id"))
    event.update(
        {
            "token": cred_db.get("token"),
            "org_id": cred_db.get("org_id"),
            "user_name": cred_db.get("user_name")
        }
    )
    event.update(event_db)
    
    callback_id = event.get("callback_id")
    command_handler(callback_id, event, db)
