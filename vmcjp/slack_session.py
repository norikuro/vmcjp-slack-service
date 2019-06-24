import json
import os
import logging
import datetime
import ipaddress
import atexit
import requests

from vmcjp.utils.slack_post import post
from vmcjp.utils.s3utils import read_json_from_s3
from vmcjp.utils import dbutils2
from vmcjp.utils import constant

logger = logging.getLogger()
logger.setLevel(logging.INFO)

help_message = "May I help you? please type `help` command."

def read_db(db, user):
    past = (
        datetime.datetime.now() - datetime.timedelta(minutes=5)
    ).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    result = db.find({"start_time": {"$gt": past}, "_id": user})
    logging.info(result)
    return result
#    return db.find({"start_time": {"$gt": past}, "_id": user})

def write_db(db, user, data):
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    data.update({"start_time": now})
#    logging.info(event)
    db.upsert({"_id": user}, {"$set": data})

def delete_db(db, user):
    db.remove({"_id": user})

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

def event_handler(event):
    db = dbutils2.DocmentDb(event["db_url"], constant.USER)
    
    user = event["user"]
    text = event["text"]
    url = event["response_url"]
    bot_token = event["bot_token"]
    
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    
    result = read_db(db, event["user"])
    if result is None:
        if "create sddc" in text:
            data["text"] = "OK, starting create sddc wizard."
            response = post(url, data, bot_token)
            data["text"] = "This conversation will end with typing `cancel` or doing nothing within 5 minutes"
            response = post(url, data, bot_token)
            data["text"] = "Please enter SDDC name"
            response = post(url, data, bot_token)
            write_db(db, user, {"command": "create_sddc"})
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
            delete_db(db, event["user"])
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
            if result["command"] == "create_sddc":
                data["text"] = "Single host or Multi host?"
                response = post(url, data, bot_token)
                write_db(db, user, {"command": "sddc_name", "sddc_name": text})
                return
            else:
                return
#    logging.info(response.read())

def is_valid_network(address):
    try:
        ipaddress.ip_network(address)
        return True
    except ValueError:
        return False

def lambda_handler(event, context):
#    logging.info(event)
    f = json.load(open(constant.S3_CONFIG, 'r'))
    event.update(
        {
            "db_url": read_json_from_s3(f["bucket"], f["config"])["db_url"],
            "token": f["token"],
            "org_id": f["org_id"]
        }
    )
    event_handler(event)
