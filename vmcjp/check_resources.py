import json
import requests
import atexit
import logging
import os

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.lambdautils import call_lambda
from vmcjp.utils.slack_post import post_to_response_url
from vmcjp.utils.s3utils import read_json_from_s3

from vmcjp.utils import dbutils
from vmcjp.utils import constant

#TEST_ORG_ID = os.environ["test_org"] #for test

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_config(user_name):
  db = dbutils.DocmentDb(
    constant.S3_CONFIG, 
    constant.USER_DB, 
    constant.USER_COLLECTION
  )
  
  return db.find_with_fields(
    {"_id": user_name}, 
    {
      "updated": 0,
      "_id": 0
    }
  )

def get_vmc_client():
  f = json.load(open(constant.S3_CONFIG, "r"))
  j = read_json_from_s3(f["bucket"], f["config"])
  token = j["token"]
  
  session = requests.Session()
  vmc_client = create_vmc_client(token, session=session)
  atexit.register(session.close)
  return vmc_client
  
def check(event, vmc_client):
  if not check_org(event["org_id"], vmc_client):
    return "Org with ID {} doesn't exist".format(event["org_id"])    
  if not check_sddc(event["org_id"], event["sddc_id"], vmc_client):
    return "SDDC ID {} already exists".format(event["sddc_id"])
  if not check_num_hosts(event["org_id"], event["num_hosts"], vmc_client):
    return "Maximum deployable number of hosts exeeded"
  if not check_customer_aws(event["org_id"], event["aws_account"], vmc_client):
    return "AWS Account with ID {} doesn't exist or connected to this Org".format(event["aws_account"])
  else:
    call_lambda("create_sddc", event)
    return "Checked, no pronlem. Then I will create sddc."

def check_org(org_id, vmc_client):
#  check if org is exist
  orgs = vmc_client.Orgs.list()
  if org_id not in [org.id for org in orgs]:
    return False
  return True
  
def check_sddc(org_id, sddc_id, vmc_client):
# check if sddc name and id is not already exist
#  sddcs = vmc_client.orgs.Sddcs.list(org_id)
  sddcs = vmc_client.orgs.Sddcs.list(TEST_ORG_ID)
  for sddc in sddcs:
    if sddc_id == sddc.id:
      return False
  return True

def check_num_hosts(org_id, num_hosts, vmc_client):
# check deployable number of hosts
# 1 host is for EDRS
  i = 0
#  sddcs = vmc_client.orgs.Sddcs.list(org_id)
  sddcs = vmc_client.orgs.Sddcs.list(TEST_ORG_ID) #for test  
  for sddc in sddcs:
    i = i + len(sddc.resource_config.esx_hosts)
  i = i + num_hosts
#  max_host = int(vmc_client.Orgs.get(org_id).properties.values["sddcLimit"]) - 1
  max_host = int(vmc_client.Orgs.get(TEST_ORG_ID).properties.values["sddcLimit"]) - 1
#skip following for test
#  if i >= max_host:
#    return False
  return True
  
def check_customer_aws(org_id, aws_account, vmc_client):
#  check if customer aws is exist
#  accounts = vmc_client.orgs.account_link.ConnectedAccounts.get(org_id)
  accounts = vmc_client.orgs.account_link.ConnectedAccounts.get(TEST_ORG_ID)
  for account in accounts:
    if aws_account == account.account_number:
      return True
  return False
  
#  check if customer subnet is exist
#  need to implement later, Zero Cloud happens error
#  vmc_map = vmc_client.orgs.account_link.CompatibleSubnets.get(org=event["org_id"], linked_account_id=event["connected_account_id"]).vpc_map
#  for v in vpc_map.values():
#    for subnet in v.subnets:

def lambda_handler(event, context):
#  logging.info(event)
  url = event["response_url"]
  event.update(get_config(event["user"]))
  resp = check(event, get_vmc_client())
  text = {
#    "channel": event["channel_id"],
    "text": resp
  }
  response = post_to_response_url(url, text)
#  logging.info(response.read())
#  logging.info(event)
