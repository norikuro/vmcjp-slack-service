import json
import os
import logging

from vmcjp.utils.slack_post import post_to_response_url
from vmcjp.utils import dbutils
from vmcjp.utils import constant

logger = logging.getLogger()
logger.setLevel(logging.INFO)

RESTORE_BUTTON = constant.BUTTON_DIR + "restore_button.json"

def restore_sddc():
    db = dbutils.DocmentDb(
        constant.S3_CONFIG,
        constant.SDDC_DB,
        constant.SDDC_COLLECTION
    )
    
    config = db.find_with_fields(
        {},
        {
            "org.id": 1,
            "sddc_updated": 1,
            "sddc.id": 1,
            "sddc.name": 1,
            "sddc.region": 1,
            "sddc.num_hosts": 1,
            "org.display_name": 1,
            "customer_vpc.linked_account": 1,
            "customer_vpc.linked_vpc_subnets_id": 1,
            "aws_connected_account": 1,
            "_id": 0
        }
    )
    
    ca = config["aws_connected_account"]
    for a in ca:
        if config["customer_vpc"]["linked_account"] == a["account_number"]:
            a_id = a["id"]
    
    return {
        "org_id": config["org"]["id"],
        "org_name": config["org"]["display_name"],
        "updated": config["sddc_updated"],
        "sddc_id": config["sddc"]["id"],
        "sddc_name": config["sddc"]["name"],
        "region": config["sddc"]["region"],
        "num_hosts": config["sddc"]["num_hosts"],
        "aws_account": config["customer_vpc"]["linked_account"],
        "customer_subnet_id": config["customer_vpc"]["linked_vpc_subnets_id"],
        "connected_account_id": a_id
    }

def create_button(config):
    button_set = json.load(open(RESTORE_BUTTON, 'r'))
    
    fields = [
        {
            "title": "Backed up date",
            "value": config["updated"],
            "short": "true"
        },
        {
            "title": "Org Name",
#            "value": config["org_name"],
            "value": "APJ SME Zero Cloud Org", #for test
            "short": "true"
        },
        {
            "title": "SDDC name",
#            "value": config["sddc_name"],
            "value": "nk_single_api_test", #for test
            "short": "true"
        },
        {
            "title": "Number of hosts",
#            "value": config["num_hosts"],
            "value": 3, #for test
            "short": "true"
        },
        {
            "title": "AWS account",
            "value": config["aws_account"],
            "short": "true"
        },
        {
            "title": "AWS linked subnet",
#            "value": config["customer_subnet_id"],
            "value": "subnet-4c80da05", #for test,
            "short": "true"
        },
        {
            "title": "Region",
            "value": config["region"],
            "short": "true"
        }
    ]

    button_set["attachments"][0]["fields"] = fields
#    logging.info(button_set)
    return button_set

def write_db(event, config):
    db = dbutils.DocmentDb(
        constant.S3_CONFIG,
        constant.USER_DB,
        constant.USER_COLLECTION
    )
    db.upsert({"_id": event["user"]}, {"$set": config})    

def lambda_handler(event, context):
#    logging.info(event)
    
    url = event["response_url"]
    config = restore_sddc()
    button = create_button(config)
    
    response = post_to_response_url(url, button)
    
    write_db(event, config)
#    logging.info(response.read())
