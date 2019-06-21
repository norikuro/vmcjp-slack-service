import json
import os
import logging
import datetime

from vmcjp.utils.slack_post import post
from vmcjp.utils import dbutils
from vmcjp.utils import constant

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#EXPECTED_TOKEN = os.environ["token"]
#BOT_OAUTH_TOKEN = os.environ["bot_token"]

def write_db(event):
    db = dbutils.DocmentDb(
        constant.S3_CONFIG,
        constant.USER_DB,
        constant.USER_COLLECTION
    )
    event.update({"start_time": datetime.datetime.now().strftime('%s')})
    logging.info(event)
    db.upsert({"_id": event.pop("user")}, {"$set": event})
    
def lambda_handler(event, context):
#    logging.info(event)
    
    if event["event_type"] == "sddc_name":
        write_db(event)
