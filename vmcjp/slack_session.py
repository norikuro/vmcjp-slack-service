import json
import os
import logging
import datetime
import ipaddress
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.slack_post import post
from vmcjp.utils.s3utils import read_json_from_s3
from vmcjp.utils import dbutils2
from vmcjp.utils import constant
from vmcjp.slack_event import event_handler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
#    logging.info(event)
    f = json.load(open(constant.S3_CONFIG, 'r'))
    j = read_json_from_s3(f["bucket"], f["config"])
    
    event.update(
        {
            "db_url": j["db_url"],
            "token": j["token"],
            "org_id": j["org_id"]
        }
    )
    
    if event.has_key("callback_id"):
        aaa
    else:
        event_handler(event)
