import json
import os
import logging

from vmcjp.utils.slack_post import post_field_button
from vmcjp.utils import sddc_db
from vmcjp.utils import constant

logger = logging.getLogger()
logger.setLevel(logging.INFO)

RESTORE_BUTTON = constant.BUTTON_DIR + "restore.json"

def get_backedup_sddc_config(db):    
    config = db.find_with_fields(
        {},
        {
            "org.id": 1,
            "sddc_updated": 1,
            "sddc.id": 1,
            "sddc.name": 1,
            "sddc.region": 1,
            "sddc.num_hosts": 1,
            "vpc_cidr": 1,
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
        "vpc_cidr": config["sddc"]["vpc_cidr"]
        "aws_account": config["customer_vpc"]["linked_account"],
        "customer_subnet_id": config["customer_vpc"]["linked_vpc_subnets_id"],
        "connected_account_id": a_id
    }

def lambda_handler(event, context):
#    logging.info(event)
    db = sddc_db.DocmentDb(url)
    event.update(get_backedup_sddc_config(db))
    response = post_field_button(event, RESTORE_BUTTON)
#    logging.info(response.read())
