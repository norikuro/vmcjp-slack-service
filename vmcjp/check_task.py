import json
import os
import logging
import requests
import atexit

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.s3utils import read_json_from_s3
from vmcjp.utils.cloudwatch import remove_event
from vmcjp.utils.task_helper import task_handler

from vmcjp.utils import constant

TEST_ORG_ID = os.environ["test_org"] #for test

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_vmc_client(token):  
  session = requests.Session()
  vmc_client = create_vmc_client(token, session=session)
  atexit.register(session.close)
  return vmc_client

def lambda_handler(event, context):
    logging.info(event)
#    f = json.load(open(constant.S3_CONFIG, "r"))
#    j = read_json_from_s3(f["bucket"], f["config"])

    vmc_client = get_vmc_client(event.get("token"))
    db = dbutils2.DocmentDb(event.get("db_url"))
    db.read_event_db(user_id)
    
    if "task_started" in event.get("command"):
      event.update(
        {"command": "task_progress"}
      )
      status = task_handler(
        vmc_client.orgs.Tasks, 
        event
      ),
      response = post_text(
        event,
        status
        "bot"
      )
      if "Failed" in status:
        aa
      elif "Canceled" in status:
        aaa
      elif "Finished" in status:
        aaaa
    else:
      remove_event(event["event_name"], event["lambda_name"])
      task_handler(vmc_client.orgs.Tasks, event)
