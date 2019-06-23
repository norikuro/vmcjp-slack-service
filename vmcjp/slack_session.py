import json
import os
import logging
import datetime

from vmcjp.utils.slack_post import post
from vmcjp.utils import dbutils
from vmcjp.utils import constant

logger = logging.getLogger()
logger.setLevel(logging.INFO)

EXPECTED_TOKEN = os.environ["token"]
BOT_OAUTH_TOKEN = os.environ["bot_token"]

def read_db(event):
    db = dbutils.DocmentDb(
        constant.S3_CONFIG,
        constant.USER_DB,
        constant.USER_COLLECTION
    )
    
    past = (
        datetime.datetime.now() - datetime.timedelta(minutes=5)
    ).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    return db.find({"start_time": {"$gt": past}, "user": event["user"]})

def write_db(event):
    db = dbutils.DocmentDb(
        constant.S3_CONFIG,
        constant.USER_DB,
        constant.USER_COLLECTION
    )
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    event.update({"start_time": now})
#    logging.info(event)
    db.upsert({"_id": event.pop("user")}, {"$set": event})
    
def event_handler(event):
    if "create sddc" in text:
        data["text"] = "OK, starting create sddc wizard."
        response = post(url, data, BOT_OAUTH_TOKEN)
        data["text"] = "This conversation will end with typing `cancel` or doing nothing within 5 minutes"
        response = post(url, data, BOT_OAUTH_TOKEN)
        data["text"] = "Please enter SDDC name"
        response = post(url, data, BOT_OAUTH_TOKEN)
        le.update({"event_type": "create_sddc"})
        call_lambda("slack_session", le)
    elif "cancel" in text:
        data["text"] = "OK, create SDDC has cenceled."
        response = post(url, data, BOT_OAUTH_TOKEN)
        le.update({"event_type": "cancel"})
        call_lambda("slack_session", le)
    elif text.find(" ") != -1:
        data["text"] = event
        response = post(url, data, BOT_OAUTH_TOKEN)
    elif is_valid_network(text):
        data["text"] = text
        response = post(url, data, BOT_OAUTH_TOKEN)
    else:
        data["text"] = "Single host or Multi host?"
        response = post(url, data, BOT_OAUTH_TOKEN)
        le.update({"event_type": "sddc_name"})
        call_lambda("slack_session", le)
#    logging.info(response.read())

def lambda_handler(event, context):
#    logging.info(event)
    event_handler(event)
