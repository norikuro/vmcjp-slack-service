import json
import os
import logging

from vmcjp.utils import dbutils2
from vmcjp.utils import constant
from vmcjp import slack_message

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
#    logging.info(event)
    db = dbutils2.DocmentDb(event.get("db_url"))
    db.init_sddc_db()
    config = db.get_backedup_sddc_config()
    
    event.update(config)
    db.write_event_db(event.get("user_id"), config)
    
    slack_message.restore_message(event)
#    logging.info(response.read())
