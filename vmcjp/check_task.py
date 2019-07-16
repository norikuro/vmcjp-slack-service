import json
import logging
import requests
import atexit

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.cloudwatch import remove_event
from vmcjp.utils.task_helper import task_handler
from vmcjp.utils.slack_post import post_to_webhook
#from vmcjp.utils.slack_post import post_text, post_to_webhook
from vmcjp.utils import dbutils2
from vmcjp import slack_message

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_vmc_client(token):  
  session = requests.Session()
  vmc_client = create_vmc_client(token, session=session)
  atexit.register(session.close)
  return vmc_client

def lambda_handler(event, context):
#    logging.info(event)
    db = dbutils2.DocmentDb(event.get("db_url"))

    if "task_started" in event.get("status"):
      event.update(
        {"status": "task_progress"}
      )
    elif "task_failed" in event.get("status"):
      db.delete_event_db(event.get("user_id"))
      return
    else:
      remove_event(
        event.get("event_name"), 
        event.get("lambda_name")
      )
      
    vmc_client = get_vmc_client(event.get("token"))
    status = task_handler(
      vmc_client.orgs.Tasks, 
      event
    )
    event.update({"status": status})
    slack_message.check_task_message(event)
#    response = post_text(
#      event,
#      status,
#      "bot"
#    )
    slack_message.check_task_webhook_message(event)
#    response = post_to_webhook(
#      event.get("webhook_url"), 
#      status
#    )

    if "Failed" in status or "Canceled" in status or "Finished" in status:
      db.delete_event_db(event.get("user_id"))
