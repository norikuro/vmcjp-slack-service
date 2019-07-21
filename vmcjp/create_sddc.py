import json
import os
import logging
import requests
import atexit

from distutils.util import strtobool
from com.vmware.vmc.model_client import AwsSddcConfig, AccountLinkSddcConfig, SddcConfig, AccountLinkConfig, ErrorResponse
from com.vmware.vapi.std.errors_client import Error, InvalidRequest
from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.lambdautils import call_lambda
from vmcjp.utils import constant
from vmcjp.utils.metadata import get_members
from vmcjp import slack_message

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
  provider,
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
    provider=provider,
#    provider="ZEROCLOUD", #for test
#    provider=SddcConfig.PROVIDER_AWS,
    num_hosts=num_hosts,
    account_link_config=None if link_aws else AccountLinkConfig(True),
    deployment_type=SddcConfig.DEPLOYMENT_TYPE_SINGLEAZ
  )
  
  try:
    task = vmc_client.orgs.Sddcs.create(
      org=org_id, sddc_config=sddc_config
    )
#    return {
#      "success": True,
#      "task_id": task.id
#    }
    return task.id
  except InvalidRequest as err:
    error_response = err.data.convert_to(ErrorResponse)
    raise Exception(error_response.error_messages)
#    messages = error_response.error_messages
#    for message in messages:
#      logger.error(message)
#    if len(messages) > 0:
#        message = messages[0]
#    return {
#      "success": False,
#      "message": "Failed to create sddc.  {}".format(message)
#    }
#  return { # for test
#      "success": True,
#      "task_id": "xxxxxxxxx"
#  }

def lambda_handler(event, context):
#  logging.info(event)
  event.update({"lambda_name": "check_task"})

  vmc_client = get_vmc_client(event.get("token"))  
#  result = create_sddc(
#    event.get("org_id"),
#    event.get("region"),
#    event.get("sddc_name"),
#    event.get("sddc_type"),
#    event.get("vpc_cidr"),
#    event.get("provider"),
#    event.get("customer_subnet_id"),
#    event.get("connected_account_id"),
#    event.get("num_hosts"),
#    strtobool(event.get("link_aws")) == 1,
#    vmc_client
#  )
  try:
    result = create_sddc(
      event.get("org_id"),
      event.get("region"),
      event.get("sddc_name"),
      event.get("sddc_type"),
      event.get("vpc_cidr"),
      event.get("provider"),
      event.get("customer_subnet_id"),
      event.get("connected_account_id"),
      event.get("num_hosts"),
      strtobool(event.get("link_aws")) == 1,
      vmc_client
    )
    event.update({"task_id": result})
  catch Exception as e:
    event.update(
      {
        "message": e.message,
        "status": "task_failed"
      }
    )
  
#  if result.get("success"):
#    event.update({"task_id": result.get("task_id")})
#  else:
#    event.update(
#      {
#        "message": result.get("message"),
#        "status": "task_failed"
#      }
#    )
    slack_message.crud_sddc_result_message(event)
    call_lambda("check_task", event)
    return
  
  logging.info(event) #need this log to ckech config later.
  
  slack_message.task_message(event)
  slack_message.started_crud_sddc_message(event)
  slack_message.task_webhook_message(event)
  
  event.update(
    {"status": "task_started"}
   )
  call_lambda("check_task", event)
