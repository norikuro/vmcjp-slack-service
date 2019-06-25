import os
import logging

from vmcjp.utils import dbutils2
from vmcjp.utils import constant

help_message = "May I help you? please type `help` command."

TEST_ORG_ID = os.environ["test_org"] #for test
#BUTTON = "vmcjp/precheck_button.json"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def interactive_handler(event):
    db = dbutils2.DocmentDb(event["db_url"], constant.USER)
    
    user_id = event["user_id"]
    text = event["text"]
    url = event["response_url"]
    bot_token = event["bot_token"]
    token = event["token"]
    org_id = event["org_id"]
    
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    
    result = db.read_event_db(event["user_id"])
    if result is None:
      aaa
    else:
      aaa
