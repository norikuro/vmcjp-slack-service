import json
import os
#import logging

from vmcjp.utils import constant
from vmcjp.utils.s3utils import read_json_from_s3
#from vmcjp.slack.event import event_handler
from vmcjp.slack.event2 import event_handler
#from vmcjp.slack.interactive import interactive_handler
from vmcjp.slack.interactive2 import interactive_handler

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)

def lambda_handler(event, context):
#    logging.info(event)
    f = json.load(open(constant.S3_CONFIG, 'r'))
    j = read_json_from_s3(f["bucket"], f["config"])
    
    event.update(
        {
            "db_url": j.get("db_url"),
            "aws_internal_account": os.environ["aws_account"], #for internal use
            "aws_internal_id": os.environ["aws_id"], #for internal use
            "cloudwatch_account": j.get("cloudwatch_account"), #for internal use
            "webhook_url": j.get("webhook_url"),
            "bot_token": j.get("bot_token")
        }
    )
#    logging.info(event)
    
    if event.has_key("callback_id"):
        interactive_handler(event)
    else:
        event_handler(event)
