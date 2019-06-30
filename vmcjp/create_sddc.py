import json
import os
import logging
import requests
import atexit

from com.vmware.vmc.model_client import AwsSddcConfig, AccountLinkSddcConfig, SddcConfig
from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.slack_post import post_to_webhook, post_field_button
from vmcjp.utils.task_helper import task_handler

from vmcjp.utils import constant

TEST_ORG_ID = os.environ["test_org"] #for test
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
  sddc_name,
  region,
  vpc_cidr,
  customer_subnet_id,
  connected_account_id,
  num_hosts,
  vmc_client
):  
  sddc_config = AwsSddcConfig(
    region=region,
    name="nk_single_api_test", #for test
#    name=sddc_name,
    account_link_sddc_config=[
      AccountLinkSddcConfig(
        customer_subnet_ids=[customer_subnet_id],
        connected_account_id=connected_account_id
      )
    ],
    provider="ZEROCLOUD", #for test
#    provider=SddcConfig.PROVIDER_AWS,
#    num_hosts=num_hosts,
    num_hosts=3, #for test
    deployment_type=SddcConfig.DEPLOYMENT_TYPE_SINGLEAZ
  )

#  return vmc_client.orgs.Sddcs.create(
##    org=org_id, sddc_config=sddc_config
#    TEST_ORG_ID, sddc_config=sddc_config
#  )

def lambda_handler(event, context):
#  logging.info(event)
  vmc_client = get_vmc_client(event.get("token"))
  
  task = create_sddc(
    event.get("org_id"),
    event.get("sddc_name"),
    event.get("region"),
    event.get("vpc_cidr"),
    event.get("customer_subnet_id"),
    event.get("connected_account_id"),
    event.get("num_hosts"),
    vmc_client
  )
  
#  event["task_id"] = task.id
  event["task_id"] = "xxxxxxxx"
  event["lambda_name"] = "check_task"

#  response = post_to_webhook(
#    event.get("webhook_url"), 
#    text
#  )
  
  response = post_field_button(
    event, 
    TASK_BUTTON, 
    "Hi <@{}>, started to create sddc".format(event["user_id"]), 
    type="bot"
  )
  
#  logging.info(response.read())
    
  text = {
    "text": task_handler(
      vmc_client.orgs.Tasks, 
      event
    )
  }
#  response = post_to_webhook(
#    event.get("slack_webhook_url"), 
#    text
#  )
  response = post_text(
    event,
    text,
    "bot"
  )
#  logging.info(response.read())
#  logging.info(event)
