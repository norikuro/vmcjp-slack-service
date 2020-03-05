import json
import os
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
            "db_url": j.get("db_url"),
#            "org_id": j.get("org_id"),
#            "org_id": os.environ["test_org"], #for test
            "aws_internal_account": os.environ["aws_account"], #for internal use
            "aws_internal_id": os.environ["aws_id"], #for internal use
            "cloudwatch_account": j.get("cloudwatch_account"),
            "webhook_url": j.get("webhook_url"),
            "db_url": j.get("db_url")
        }
    )
    logging.info(event)
    
    if event.has_key("callback_id"):
        interactive_handler(event)
    else:
        event_handler(event)
