def interactive_handler(event):
    user_id = event.get("user_id")
    
    db = dbutils.DocmentDb(event.get("db_url"))
    event_db = db.read_event_db(user_id, 5)
    
    if result is None:
      message_handler(constant.MAY_I, event)
      return
    
    cred_db = db.read_cred_db(event.get("user_id"))
    event.update(
        {
            "token": cred_db.get("token"),
            "org_id": cred_db.get("org_id")
        }
    )
