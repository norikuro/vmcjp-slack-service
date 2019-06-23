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

def read_db(db, event):
    past = (
        datetime.datetime.now() - datetime.timedelta(minutes=5)
    ).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    return db.find({"start_time": {"$gt": past}, "user": event["user"]})

def write_db(db, event):
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    event.update({"start_time": now})
#    logging.info(event)
    db.upsert({"_id": event.pop("user")}, {"$set": event})
    
def event_handler(event):
    db = dbutils.DocmentDb(
        constant.S3_CONFIG,
        constant.USER_DB,
        constant.USER_COLLECTION
    )
    
    url = event["response_url"]
    bot_token = event["bot_token"]
    
    data = {
        "token": event["token"],
        "channel": event["event"]["channel"]
    }
    
    if "create sddc" in text:
        data["text"] = "OK, starting create sddc wizard."
        response = post(url, data, bot_token)
        data["text"] = "This conversation will end with typing `cancel` or doing nothing within 5 minutes"
        response = post(url, data, bot_token)
        data["text"] = "Please enter SDDC name"
        response = post(url, data, bot_token)
    elif "cancel" in text:
        data["text"] = "OK, create SDDC has cenceled."
        response = post(url, data, bot_token)
    elif text.find(" ") != -1:
        data["text"] = event
        response = post(url, data, bot_token)
    elif is_valid_network(text):
        data["text"] = text
        response = post(url, data, bot_token)
    else:
        data["text"] = "Single host or Multi host?"
        response = post(url, data, bot_token)
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
