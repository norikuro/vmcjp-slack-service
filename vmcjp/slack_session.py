import json
import logging

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
        print("aa")
    else:
        event_handler(event)
