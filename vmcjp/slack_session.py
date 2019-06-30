import json
import logging

from vmcjp.utils import constant
from vmcjp.utils.s3utils import read_json_from_s3
from vmcjp.slack_event import event_handler
from vmcjp.slack_interactive import interactive_handler

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
            "org_id": j["org_id"],
            "cloudwatch_account": j["cloudwatch_account"]
        }
    )
    
    if event.has_key("callback_id"):
        interactive_handler(event)
    else:
        event_handler(event)
