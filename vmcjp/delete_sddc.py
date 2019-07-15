import json
import os
import logging
import requests
import atexit

from vmware.vapi.vmc.client import create_vmc_client
from com.vmware.vapi.std.errors_client import Unauthorized
from vmcjp.utils.slack_post import post_field_button, post_to_webhook
#from vmcjp.utils.slack_post import post_text, post_field_button, post_to_webhook
from vmcjp.utils.task_helper import task_handler
from vmcjp.utils.lambdautils import call_lambda
from vmcjp.utils import constant
from vmcjp import slack_message

TASK_BUTTON = constant.BUTTON_DIR + "task.json"

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

  try:
    task = vmc_client.orgs.Sddcs.delete(
      org=org_id, 
      sddc=sddc_id
    )
    return {
      "success": True,
      "task_id": task.id
    }
  except Unauthorized:
    return {
      "success": False,
      "message": "Failed, you are not authorized to delete sddc."
    }
  except:
    return {
      "success": False,
      "message": "Something wrong, failed to delete sddc."
    }

def lambda_handler(event, context):
#  logging.info(event)
  vmc_client = get_vmc_client(event.get("token"))
  
  result = delete_sddc(
    event.get("org_id"),
    event.get("sddc_id"),
    vmc_client
  )
  if result.get("success"):
    event.update({"task_id": result.get("task_id")})
  else:
    event.update({"message": result.get("message")})
    slack_message.crud_sddc_result_message(event)
#    response = post_text(
#      event,
#      result.get("message"),
#      "bot"
#    )
    return 
  
#  event.update({"task_id": task.id})
  event.update({"lambda_name": "check_task"})
  event.update({"command": "delete"})

  response = post_field_button(
    event, 
    TASK_BUTTON, 
    type="bot"
  )
#  logging.info(response.read())

  slack_message.started_crud_sddc_message(event)
#  response = post_to_webhook(
#    event.get("webhook_url"), 
#    "Hi <@{}>, started to delete sddc.".format(
#      event.get("user_id")
#    )
#  )
#  logging.info(response.read())  
  response = post_field_button(
    event, 
    TASK_BUTTON, 
    type="webhook"
  )
#  logging.info(response.read())

  event.update(
    {"status": "task_started"}
   )
  call_lambda("check_task", event)
