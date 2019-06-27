import json
import os
import logging
import ipaddress
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.slack_post import post, post_text, post_button
from vmcjp.utils import dbutils2
from vmcjp.utils import constant

help_message = "May I help you? please type `help`."

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
        i += len(sddc.resource_config.esx_hosts)
#    max_hosts = (int(vmc_client.Orgs.get(org_id).properties.values["sddcLimit"]) - 1) - i
    max_hosts = (int(vmc_client.Orgs.get(TEST_ORG_ID).properties.values["sddcLimit"]) - 1) - i
#    if max_hosts < 1:
#        return max_hosts
#    else:
#        return 1 if max_hosts < 3 else max_hosts
    return 4 # for test

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
    text = event["text"].lower()
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    
    db = dbutils2.DocmentDb(event["db_url"], constant.USER)
    result = db.read_event_db(event["user_id"])
    if result is None:
        if "create sddc" in text:
            post_text(
                event,
                "OK, starting create sddc wizard.",
                False
            )
            post_text(
                event,
                "This conversation will end by typing `cancel` or doing nothing for 5 minutes",
                False
            )
            post_text(
                event,
                "Checking current resources...",
                False
            )
            max_hosts = get_max_num_hosts(event["token"], event["org_id"])
            logging.info(max_hosts)
            if max_hosts < 1:
                post_text(
                    event,
                    "Sorry, we don't have enough space to deploy hosts on this org.",
                    False
                )
                post_text(
                    event,
                    "Canceled to create sddc.",
                    False
                )
                db.delete_event_db(event["user_id"])
                return
#            max_hosts = 10 #for test
            post_text(
                event,
                "You can deploy max {} hosts.".format(
                    max_hosts
                ),
                False
            )
#            button_set = json.load(open(PRECHECK_BUTTON, 'r'))
#            data.update(button_set)
#            response = post(event["post_url"], data, event["bot_token"])
            post_button(event, PRECHECK_BUTTON, False)
            db.write_event_db(
                event["user_id"], 
                {
                    "command": "create_sddc", 
                    "max_hosts": max_hosts
                }
            )
            return
        else:
            post_text(event, help_message, False)
            return
    else:
        if "create sddc" in text:
            return
        elif "cancel" in text:
            post_text(
                event,
                "OK, create SDDC has cenceled.",
                False
            )
            db.delete_event_db(event["user_id"])
            return
        elif text.find(" ") != -1:
            return
        elif is_valid_network(text):
            if result["command"] == "link_aws" or "subnet":
                post_text(
                    event,
                    "Creating sddc....",
                    False
                )
                db.write_event_db(
                    event["user_id"], 
                    {
                        "command": "vpc_cidr", 
                        "vpc_cidr": event["text"]
                    }
                )
                return
            else:
                return
        else:
            if result["command"] == "region":
                if result["max_hosts"] == 1:
#                    button_set = json.load(open(LINK_AWS_BUTTON, 'r'))
#                    data.update(button_set)
                    post_button(event, LINK_AWS_BUTTON, False)
                else:
#                    button_set = json.load(open(SINGLE_MULTI_BUTTON, 'r'))
#                    data.update(button_set)
                    post_button(event, SINGLE_MULTI_BUTTON, False)
#                response = post(event["post_url"], data, event["bot_token"])
                db.write_event_db(
                    event["user_id"], 
                    {
                        "command": "sddc_name", 
                        "sddc_name": event["text"]
                    }
                )
                return
            else:
                return
#    logging.info(response.read())
