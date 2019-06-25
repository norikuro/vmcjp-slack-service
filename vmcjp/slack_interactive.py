import os
import logging

from vmcjp.utils import dbutils2
from vmcjp.utils import constant
from vmcjp.utils.slack_post import post, post_to_response_url

help_message = "May I help you? please type `help` command."

TEST_ORG_ID = os.environ["test_org"] #for test
#BUTTON = "vmcjp/precheck_button.json"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def interactive_handler(event):
    db = dbutils2.DocmentDb(event["db_url"], constant.USER)
    
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    
    if event["callback_id"] == "create_sddc":
        if event["response"] == "yes":
            data["text"] = "Please enter SDDC name"
            response = post_to_response_url(event["response_url"], data)
            return
        else:
            data["text"] = "OK, create SDDC has cenceled."
            response = post_to_response_url(event["response_url"], data)
            db.delete_event_db(event["user_id"])
            return
