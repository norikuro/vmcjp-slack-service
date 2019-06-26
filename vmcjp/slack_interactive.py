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
    
    user_id = event["user_id"]
    
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
            db.delete_event_db(user_id)
            return
    elif event["callback_id"] == "link_aws_sddc":
        if event["response"] == "yes":
            data["text"] = "Please select aws account id which you want to link."
            response = post_to_response_url(event["response_url"], data)
        else:
            data["text"] = "Please enter CIDR block for management subnet."
            response = post_to_response_url(event["response_url"], data)
            data["text"] = "/23 is max 27 hosts, /20 is max 251, /16 is 4091."
            response = post_to_response_url(event["response_url"], data)
            data["text"] = "You can not use 10.0.0.0/15 and 172.31.0.0/16 which are reserved."
            response = post_to_response_url(event["response_url"], data)
        db.write_event_db(user_id, {"command": "link_aws", "num_hosts": 1})
