import json
import os
import logging
import ipaddress
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.slack_post import post
from vmcjp.utils import dbutils2
from vmcjp.utils import constant

help_message = "May I help you? please type `help` command."

TEST_ORG_ID = os.environ["test_org"] #for test
PRECHECK_BUTTON = constant.BUTTON_DIR + "precheck_button.json"
LINK_AWS_BUTTON = constant.BUTTON_DIR + "link_aws_button.json"
SINGLE_MULTI_BUTTON = constant.BUTTON_DIR + "single_multi_button.json"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_max_num_hosts(token, org_id):
# get deployable number of hosts
# 1 host is for Storage EDRS
    
    vmc_client = get_vmc_client(token)
    
#    sddcs = vmc_client.orgs.Sddcs.list(org_id)
    sddcs = vmc_client.orgs.Sddcs.list(TEST_ORG_ID) #for test 
    
    i = 0
    for sddc in sddcs:
        i = i + len(sddc.resource_config.esx_hosts)
#    max_host = int(vmc_client.Orgs.get(org_id).properties.values["sddcLimit"]) - 1
    max_host = int(vmc_client.Orgs.get(TEST_ORG_ID).properties.values["sddcLimit"]) - 1
    
    return max_host - i

def get_vmc_client(token):
    session = requests.Session()
    vmc_client = create_vmc_client(token, session=session)
    atexit.register(session.close)
    return vmc_client

def is_valid_network(address):
    try:
        ipaddress.ip_network(address)
        return True
    except ValueError:
        return False

def event_handler(event):
    db = dbutils2.DocmentDb(event["db_url"], constant.USER)
    
    user_id = event["user_id"]
    text = event["text"]
    url = event["response_url"]
    bot_token = event["bot_token"]
    token = event["token"]
    org_id = event["org_id"]
    
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    
    result = db.read_event_db(event["user_id"])
    if result is None:
        if "create sddc" in text:
            data["text"] = "OK, starting create sddc wizard."
            response = post(url, data, bot_token)
            data["text"] = "This conversation will end by typing `cancel` or doing nothing for 5 minutes"
            response = post(url, data, bot_token)
            data["text"] = "Checking current resources..."
            response = post(url, data, bot_token)
            max_hosts = get_max_num_hosts(token, org_id)
            max_hosts = 1 if max_hosts < 3 else max_hosts
#            max_hosts = 10 #for test
            data["text"] = "You can deploy max {} hosts.".format(
                max_hosts
            )
            button_set = json.load(open(PRECHECK_BUTTON, 'r'))
            data.update(button_set)
            response = post(url, data, bot_token)
            db.write_event_db(
                user_id, 
                {
                    "command": "create_sddc", 
                    "max_hosts": max_hosts
                }
            )
            return
        else:
            data["text"] = help_message
            response = post(url, data, bot_token)
            return
    else:
        if "create sddc" in text:
            return
        elif "cancel" in text:
            data["text"] = "OK, create SDDC has cenceled."
            response = post(url, data, bot_token)
            db.delete_event_db(event["user_id"])
            return
        elif text.find(" ") != -1:
            return
        elif is_valid_network(text):
            if result["command"] == "mgmt_cidr":
                data["text"] = "creating sddc...."
                response = post(url, data, bot_token)
                return
            else:
                return
        else:
            if result["command"] == "region":
                if result["max_hosts"] == 1:
                    button_set = json.load(open(LINK_AWS_BUTTON, 'r'))
                    data.update(button_set)
                else:
                    button_set = json.load(open(SINGLE_MULTI_BUTTON, 'r'))
                    data.update(button_set)
                response = post(url, data, bot_token)
                db.write_event_db(
                    user_id, 
                    {
                        "command": "sddc_name", 
                        "sddc_name": text
                    }
                )
                return
            else:
                return
#    logging.info(response.read())
