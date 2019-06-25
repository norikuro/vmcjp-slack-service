import os
import logging

from vmcjp.utils import dbutils2
from vmcjp.utils import constant
from vmcjp.utils.slack_post import post_to_response_url

help_message = "May I help you? please type `help` command."

TEST_ORG_ID = os.environ["test_org"] #for test
#BUTTON = "vmcjp/precheck_button.json"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def interactive_handler(event):
    db = dbutils2.DocmentDb(event["db_url"], constant.USER)
    
    user_id = event["user_id"]
#    text = event["text"]
    url = event["response_url"]
    bot_token = event["bot_token"]
    token = event["token"]
    org_id = event["org_id"]
    callback_id = event["callback_id"]
    event_response = event["response"]
#    logging.info(callback_id)
#    logging.info(event_response)
    
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    
    result = db.read_event_db(event["user_id"])
    if result is None:
      if callback_id == "create_sddc":
        if event_response == "yes":
            data["text"] = "Please enter SDDC name"
            response = post(url, data, bot_token)
#            response = post_to_response_url(url, data)
            logging.info(response.read())
            return
        else:
            data["text"] = "OK, create SDDC has cenceled."
            response = post_to_response_url(url, data)
            return
#    else:
#      aaa
