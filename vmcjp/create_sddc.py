import json
import os
import logging
import requests
import atexit

from distutils.util import strtobool
from com.vmware.vmc.model_client import AwsSddcConfig, AccountLinkSddcConfig, SddcConfig, AccountLinkConfig, ErrorResponse
from com.vmware.vapi.std.errors_client import InvalidRequest
from vmware.vapi.vmc.client import create_vmc_client

from vmcjp.utils.lambdautils import call_lambda
from vmcjp.utils import constant
from vmcjp.slack.message import messages

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
    num_hosts=num_hosts,
    account_link_config=None if link_aws else AccountLinkConfig(True),
    deployment_type=SddcConfig.DEPLOYMENT_TYPE_SINGLEAZ
  )
  
  try:
    task = vmc_client.orgs.Sddcs.create(
      org=org_id, sddc_config=sddc_config
    )
  except InvalidRequest as err:
    error_response = err.data.convert_to(ErrorResponse)
    messages = error_response.error_messages
    message = None if len(messages) <= 0 else messages[0]
    raise Exception(message)
  return task.id

def lambda_handler(event, context):
#  logging.info(event)
  event.update({"lambda_name": "check_task"})

  vmc_client = get_vmc_client(event.get("token"))  
  try:
    task = create_sddc(
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
    event.update(
      {"task_id": task}
    )
  except Exception as e:
    event.update(
      {
        "message": "Sorry, failed to create sddc.  {}".format(e.message),
        "status": "task_failed"
      }
    )
    messages.crud_sddc_result_message(event)
    call_lambda("check_task", event)
    return
  
  logging.info(event) #need this log to ckech config later.
  
  messages.task_message(event)
  messages.started_crud_sddc_message(event)
  messages.task_webhook_message(event)
  
  event.update(
    {"status": "task_started"}
   )
  call_lambda("check_task", event)
