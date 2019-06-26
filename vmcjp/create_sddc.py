import json
import os
import logging
import requests
import atexit

from com.vmware.vmc.model_client import AwsSddcConfig, AccountLinkSddcConfig, SddcConfig
from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.slack_post import post_to_webhook
from vmcjp.utils.task_helper import task_handler
from vmcjp.utils.s3utils import read_json_from_s3

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
  customer_subnet_id,
  connected_account_id,
  num_hosts,
  vmc_client
):  
  sddc_config = AwsSddcConfig(
    region="AP_NORTHEAST_1",
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

def create_button(user_id, sddc_name, task_id):
    button_set = json.load(open(TASK_BUTTON, 'r'))
    
    pretext = "Hi <@{}>, started to create sddc".format(user_id)
    fields = [
        {
            "title": "SDDC name",
            "value": sddc_name,
            "short": "true"
        },
        {
            "title": "Task id",
            "value": task_id,
            "short": "true"
        }
    ]
      
    button_set["attachments"][0]["pretext"] = pretext
    button_set["attachments"][0]["fields"] = fields
    return button_set    

def lambda_handler(event, context):
#  logging.info(event)
  
  f = json.load(open(constant.S3_CONFIG, "r"))
  j = read_json_from_s3(f["bucket"], f["config"])
  
  vmc_client = get_vmc_client(j["token"])
  task = create_sddc(
    event["org_id"],
    event["sddc_name"],
    event.pop("customer_subnet_id"),
    event.pop("connected_account_id"),
    event.pop("num_hosts"),
    vmc_client
  )
#  logging.info(task)
  
  event.pop("sddc_id")
#  event["task_id"] = task.id
  event["task_id"] = "xxxxxxxx"
  event["lambda_name"] = "check_task"

  text = create_button(event["user_id"], event["sddc_name"], "xxxxxxxxxxx") #for test
#  text = create_button(event["user_id"], event["sddc_name"], event["task_id"])
  response = post_to_webhook(j["slack_webhook_url"], text)
#  logging.info(response.read())
    
  text = {
    "text": task_handler(
      vmc_client.orgs.Tasks, 
      event
    )
  }
  response = post_to_webhook(j["slack_webhook_url"], text)
#  logging.info(response.read())
#  logging.info(event)
