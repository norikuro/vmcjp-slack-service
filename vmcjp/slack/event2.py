from vmcjp.utils import dbutils
from vmcjp.utils import constant

def event_handler(event):
    text = event.get("text").lower()
    
    db = dbutils.DocmentDb(event.get("db_url"))
    current = db.read_event_db(event.get("user_id"), 120)
    if current is not None and current.get("status") == "creating":
        message_handler(constant.ASK_WAIT_TASK, event)
        return
    
    result = db.read_event_db(event.get("user_id"), 5)
    __cred_data = db.read_cred_db(event.get("user_id"))
    
