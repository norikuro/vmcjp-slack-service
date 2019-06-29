import json
import os
import logging
import ipaddress
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.slack_post import post, post_text, post_button, post_field_button
from vmcjp.utils import dbutils2
from vmcjp.utils import constant

help_message = "May I help you? please type `help`."

TEST_ORG_ID = os.environ["test_org"] #for test
PRECHECK_BUTTON = constant.BUTTON_DIR + "precheck_button.json"
LINK_AWS_BUTTON = constant.BUTTON_DIR + "link_aws_button.json"
SINGLE_MULTI_BUTTON = constant.BUTTON_DIR + "single_multi_button.json"
CREATE_BUTTON = constant.BUTTON_DIR + "create_button.json"

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
    max_hosts = (int(vmc_client.Orgs.get(TEST_ORG_ID).properties.values["sddcLimit"]) - 1) - i #for test
#    if max_hosts < 1:
#        return max_hosts
#    else:
#        return 1 if max_hosts < 3 else max_hosts
    return 4 #for test

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
    
def create_configmation_button(result, button):
    fields = button.get("attachments")[0].get("fields")
    for field in fields:
        field.update({"value": result.get(field.get("value"))})
    return button

def event_handler(event):
    text = event["text"].lower()
    
    db = dbutils2.DocmentDb(event["db_url"], constant.USER)
    current = db.read_event_db(event["user_id"], 120)
    if current is not None and current.get("command") == "create":
        response = post_text(
            event,
            "Creating sddc now, please wait until the task is finished.",
            "bot"
        )
#        logging.info(response.read())
        return
    
    result = db.read_event_db(event["user_id"], 5)
    if result is None:
        if "create sddc" in text:
            response = post_text(
                event,
                "OK, starting create sddc wizard.",
                "bot"
            )
#            logging.info(response.read())
            response = post_text(
                event,
                "This conversation will end by typing `cancel` or doing nothing for 5 minutes",
                "bot"
            )
#            logging.info(response.read())
            response = post_text(
                event,
                "Checking current resources...",
                "bot"
            )
#            logging.info(response.read())
            max_hosts = get_max_num_hosts(event["token"], event["org_id"])
            if max_hosts < 1:
                response = post_text(
                    event,
                    "Sorry, we don't have enough space to deploy hosts on this org.",
                    "bot"
                )
#                logging.info(response.read())
                response = post_text(
                    event,
                    "Canceled to create sddc.",
                    "bot"
                )
#                logging.info(response.read())
                db.delete_event_db(event["user_id"])
                return
            response = post_text(
                event,
                "You can deploy max {} hosts.".format(
                    max_hosts
                ),
                "bot"
            )
#            logging.info(response.read())
            response = post_button(event, PRECHECK_BUTTON, "bot")
#            logging.info(response.read())
            db.write_event_db(
                event["user_id"], 
                {
                    "command": "create_sddc", 
                    "max_hosts": max_hosts
                }
            )
        else:
            response = post_text(event, help_message, "bot")
#            logging.info(response.read())
        return
    else:
        if "create sddc" in text:
            return
        elif "cancel" in text:
            response = post_text(
                event,
                "OK, create SDDC has cenceled.",
                "bot"
            )
#            logging.info(response.read())
            db.delete_event_db(event["user_id"])
            return
        elif text.find(" ") != -1:
            return
        elif is_valid_network(text):
            if result["command"] == "link_aws" or "subnet":
                logging.info("pre event!!! " + json.dumps(event))
                logging.info("result!!! " + json.dumps(result))
                logging.info("result!!! type" + str(type(result)))
                e = event.update(result)
                logging.info("event.update!!! " + json.dumps(e))
                logging.info("event.update!!! type" + str(type(e)))
                post_field_button(
                    e, 
                    CREATE_BUTTON, 
                    "bot"
                )
#                post_text(
#                    event,
#                    "Creating sddc....",
#                    "bot"
#                )
                db.write_event_db(
                    event["user_id"], 
                    {
                        "command": "vpc_cidr", 
                        "vpc_cidr": event["text"]
                    }
                )
            return
        else:
            if result["command"] == "region":
                if result["max_hosts"] == 1:
                    response = post_button(event, LINK_AWS_BUTTON, "bot")
#                    logging.info(response.read())
                else:
                    response = post_button(event, SINGLE_MULTI_BUTTON, "bot")
#                    logging.info(response.read())
                db.write_event_db(
                    event["user_id"], 
                    {
                        "command": "sddc_name", 
                        "sddc_name": event["text"]
                    }
                )
            return
