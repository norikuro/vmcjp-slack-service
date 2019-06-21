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

def write_db(user, data):
    db = dbutils.DocmentDb(
        constant.S3_CONFIG,
        constant.USER_DB,
        constant.USER_COLLECTION
    )
    data.update({"start_time": datetime.datetime.now()})
    db.upsert({"_id": user}, {"$set": data})
