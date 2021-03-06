import requests
import atexit
#import logging

from vmware.vapi.vmc.client import create_vmc_client

from vmcjp.utils.lambdautils import call_lambda
from vmcjp.utils import dbutils
from vmcjp.utils import constant
from vmcjp.slack.messages import message_handler

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)

def get_vmc_client(token):
  session = requests.Session()
  vmc_client = create_vmc_client(token, session=session)
  atexit.register(session.close)
  return vmc_client
  
def check(event, vmc_client):
  if not check_sddc(event.get("org_id"), event.get("sddc_id"), vmc_client):
    return {
      "result": False,
      "message": "SDDC ID {} already exists".format(event.get("sddc_id"))
    }
  
  if not check_num_hosts(event.get("org_id"), event.get("num_hosts"), vmc_client):
    return {
      "result": False,
      "message": "Maximum deployable number of hosts exeeded"
    }
  
  if not check_customer_aws(event.get("org_id"), event.get("aws_account"), vmc_client):
    return {
      "result": False,
      "message": "AWS Account with ID {} doesn't exist or connected to this Org".format(event.get("aws_account"))
    }
  else:
    call_lambda("create_sddc", event)
    return {
      "result": True,
      "message": "Checked, no pronlem. Then I will create sddc."
    }

def check_sddc(org_id, sddc_id, vmc_client):
# check if sddc name and id is not already exist
  sddcs = vmc_client.orgs.Sddcs.list(org_id)
  for sddc in sddcs:
    if sddc_id == sddc.id:
      return False
  return True

def check_num_hosts(org_id, num_hosts, vmc_client):
# check deployable number of hosts
# 1 host is for EDRS
  i = 0
  sddcs = vmc_client.orgs.Sddcs.list(org_id)
  for sddc in sddcs:
    i = i + len(sddc.resource_config.esx_hosts)
  i = i + num_hosts
  max_host = int(vmc_client.Orgs.get(org_id).properties.values["sddcLimit"]) - 1
  if i >= max_host:
    return False
  return True
  
def check_customer_aws(org_id, aws_account, vmc_client):
#  check if customer aws is exist
  logging.info(org_id)
  accounts = vmc_client.orgs.account_link.ConnectedAccounts.get(org_id)
  for account in accounts:
    if aws_account == account.account_number:
      return True
  return False
  
#  check if customer subnet is exist
#  need to implement later, Zero Cloud happens error

def lambda_handler(event, context):
#  logging.info(event)

  result = check(
    event, 
    get_vmc_client(event.get("token"))
  )
  
  event.update(
    {
      "check_result": result.get("message")
    }
  )
  message_handler(constant.CHECK_RESULT, event)
  
  db = dbutils.DocmentDb(event.get("db_url"))
  if result.get("result"):
    db.write_event_db(
      event.get("user_id"), 
      {
        "command": "create",
        "status": "creating"
      }
    )
  else:
    db.delete_event_db(event.get("user_id"))
