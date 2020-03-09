from vmcjp.slack.messages import message_handler

def command_handler(com, event):
    eval(com)(event)

def register_org(event):
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
