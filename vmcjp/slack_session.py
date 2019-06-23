import json
import os
import logging
import datetime
import ipaddress

from vmcjp.utils.slack_post import post
from vmcjp.utils import dbutils
from vmcjp.utils import constant

logger = logging.getLogger()
logger.setLevel(logging.INFO)

help_message = "May I help you? please type `help` command."

def read_db(db, user):
    past = (
        datetime.datetime.now() - datetime.timedelta(minutes=5)
    ).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
#    query.update({"start_time": {"$gt": past}})
    
#    return db.find({"start_time": {"$gt": past}, "user": event["user"]})
    return db.find({"start_time": {"$gt": past}, "user": user})
#    return db.find(query)

def write_db(db, user, data):
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    data.update({"start_time": now})
#    logging.info(event)
    db.upsert({"_id": user}, {"$set": data})

def delete_db(db, user):
    write_db(db, user, null)
    
def event_handler(event):
    db = dbutils.DocmentDb(
        constant.S3_CONFIG,
        constant.USER_DB,
        constant.USER_COLLECTION
    )
    
    text = event["text"]
    url = event["response_url"]
    bot_token = event["bot_token"]
    
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    
    result = read_db(db, event["user"])
    if "create sddc" in text:
        if result is None:
            data["text"] = "OK, starting create sddc wizard."
            response = post(url, data, bot_token)
            data["text"] = "This conversation will end with typing `cancel` or doing nothing within 5 minutes"
            response = post(url, data, bot_token)
            data["text"] = "Please enter SDDC name"
            response = post(url, data, bot_token)
            write_db(db, event["user"], {"command": "create_sddc"})
            return
        else:
            return
    elif "cancel" in text:
        data["text"] = "OK, create SDDC has cenceled."
        response = post(url, data, bot_token)
        delete_db(db, event["user"])
        return
    elif text.find(" ") != -1:
        data["text"] = help_message
        response = post(url, data, bot_token)
        return
    elif is_valid_network(text):
        if result is None:
            data["text"] = help_message
            response = post(url, data, bot_token)
            return
        else:
            if result["command"] == "mgmt_cidr":
                data["text"] = "creating sddc...."
                response = post(url, data, bot_token)
                return
            else:
                return
    else:
        if result is None:
            data["text"] = help_message
            response = post(url, data, bot_token)
            return
        else:
            if result["command"] == "create_sddc":
                data["text"] = "Single host or Multi host?"
                response = post(url, data, bot_token)
                ##write something!!!
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
    event_handler(event)
