import json
import os
import logging
import requests
import atexit

from distutils.util import strtobool
from com.vmware.vmc.model_client import AwsSddcConfig, AccountLinkSddcConfig, SddcConfig, AccountLinkConfig
from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.slack_post import post_field_button
from vmcjp.utils.task_helper import task_handler
from vmcjp.utils.lambdautils import call_lambda
from vmcjp.utils import constant

TASK_BUTTON = constant.BUTTON_DIR + "task_button.json"

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
  
  return vmc_client.orgs.Sddcs.create(
    org=org_id, sddc_config=sddc_config
  )

def lambda_handler(event, context):
#  logging.info(event)
  vmc_client = get_vmc_client(event.get("token"))
  
  task = create_sddc(
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
    
  event.update({"task_id": task.id})
#  event["task_id"] = "xxxxxxxx" #for test
  event.update({"lambda_name": "check_task"})
  event.update({"command": "create"})
#  logging.info(event)

#  response = post_to_webhook(
#    event.get("webhook_url"), 
#    text
#  )
#  logging.info(response.read())
  
  response = post_field_button(
    event, 
    TASK_BUTTON, 
    "Hi <@{}>, started to create sddc".format(
      event.get("user_id")
    ), 
    type="bot"
  )
#  logging.info(response.read())

  event.update(
    {"status": "task_started"}
   )
  call_lambda("check_task", event)
