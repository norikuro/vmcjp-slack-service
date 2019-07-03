import json
import os
import logging
import requests
import atexit

#from distutils.util import strtobool
#from com.vmware.vmc.model_client import AwsSddcConfig, AccountLinkSddcConfig, SddcConfig, AccountLinkConfig
from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.slack_post import post_text, post_field_button
from vmcjp.utils.task_helper import task_handler
from vmcjp.utils import constant

TASK_BUTTON = constant.BUTTON_DIR + "task_button.json"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_vmc_client(token):  
  session = requests.Session()
  vmc_client = create_vmc_client(token, session=session)
  atexit.register(session.close)
  return vmc_client

def delete_sddc(
  org_id,
  sddc_id,
  vmc_client
):

  return vmc_client.orgs.Sddcs.delete(
    org=org_id, 
    sddc=sddc_id
  )

def lambda_handler(event, context):
#  logging.info(event)
  vmc_client = get_vmc_client(event.get("token"))
  
  task = delete_sddc(
    event.get("org_id"),
    event.get("sddc_id"),
    vmc_client
  )
    
  event.update({"task_id": task.id})
#  event["task_id"] = "xxxxxxxx" #for test
  event.update({"lambda_name": "check_task"})
  event.update({"command": "delete"})
#  logging.info(event)

#  response = post_to_webhook(
#    event.get("webhook_url"), 
#    text
#  )
#  logging.info(response.read())
  
  response = post_field_button(
    event, 
    TASK_BUTTON, 
    "Hi <@{}>, started to delete sddc".format(
      event.get("user_id")
    ), 
    type="bot"
  )
#  logging.info(response.read())
    
  response = post_text(
    event,
    task_handler(
      vmc_client.orgs.Tasks, 
      event
    ),
    "bot"
  )
#  logging.info(response.read())
