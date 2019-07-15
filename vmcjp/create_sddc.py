import json
import os
import logging
import requests
import atexit

from distutils.util import strtobool
from com.vmware.vmc.model_client import AwsSddcConfig, AccountLinkSddcConfig, SddcConfig, AccountLinkConfig
from com.vmware.vapi.std.errors_client import Unauthorized
from vmware.vapi.vmc.client import create_vmc_client
#from vmcjp.utils.slack_post import post_text, post_field_button, post_to_webhook
from vmcjp.utils.slack_post import post_field_button
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

def create_sddc(
  org_id,
  region,
  sddc_name,
  sddc_type,
  vpc_cidr,
  customer_subnet_id,
  connected_account_id,
  num_hosts,
  link_aws,
  vmc_client
):
  sddc_config = AwsSddcConfig(
    region=region,
    name=sddc_name,
    sddc_type=sddc_type,
    account_link_sddc_config=[
      AccountLinkSddcConfig(
        customer_subnet_ids=[customer_subnet_id],
        connected_account_id=connected_account_id
      )
    ] if link_aws else None,
    vpc_cidr=vpc_cidr,
    provider="ZEROCLOUD", #for test
#    provider=SddcConfig.PROVIDER_AWS,
    num_hosts=num_hosts,
    account_link_config=None if link_aws else AccountLinkConfig(True),
    deployment_type=SddcConfig.DEPLOYMENT_TYPE_SINGLEAZ
  )
  
#  try:
#    task = vmc_client.orgs.Sddcs.create(
#      org=org_id, sddc_config=sddc_config
#    )
#    return {
#      "success": True,
#      "task_id": task.id
#    }
#  except Unauthorized:
#    return {
#      "success": False,
#      "message": "Failed, you are not authorized to create sddc."
#    }
#  except:
#    return {
#      "success": False,
#      "message": "Something wrong, failed to create sddc."
#    }
  return {
    "success": False,
    "message": "Something wrong, failed to create sddc."
  }

def lambda_handler(event, context):
#  logging.info(event)
  vmc_client = get_vmc_client(event.get("token"))
  
  result = create_sddc(
    event.get("org_id"),
    event.get("region"),
    event.get("sddc_name"),
    event.get("sddc_type"),
    event.get("vpc_cidr"),
    event.get("customer_subnet_id"),
    event.get("connected_account_id"),
    event.get("num_hosts"),
    strtobool(event.get("link_aws")) == 1,
    vmc_client
  )
  
  if result.get("success"):
    event.update({"task_id": result.get("task_id")})
  else:
    event.update({"message": result.get("message")})
    event.update({"status": "task_failed"})
    slack_message.crud_sddc_result_message(event)
    call_lambda("check_task", event)
    return
  
  event.update({"lambda_name": "check_task"})
  event.update({"command": "create"})
  logging.info(event) #need this log to ckech config later.
  
  response = post_field_button(
    event, 
    TASK_BUTTON, 
    type="bot"
  )
#  logging.info(response.read())

  slack_message.started_crud_sddc_message(event)
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
