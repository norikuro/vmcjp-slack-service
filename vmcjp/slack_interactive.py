import json
import os
import logging
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client

from vmcjp.utils import dbutils2
from vmcjp.utils import constant
#from vmcjp.utils.slack_post import post, post_to_response_url
from vmcjp.utils.slack_post import post_text, post_button

help_message = "May I help you? please type `help` command."

TEST_ORG_ID = os.environ["test_org"] #for test
AWS_ACCOUNT = os.environ["aws_account"] #for internal use
AWS_ID = os.environ["aws_id"] #for internal use
ACCOUNT_BUTTON = constant.BUTTON_DIR + "account_button.json"
REGION_BUTTON = constant.BUTTON_DIR + "region_button.json"
VPC_BUTTON = constant.BUTTON_DIR + "vpc_button.json"
SUBNET_BUTTON = constant.BUTTON_DIR + "subnet_button.json"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_vmc_client(token):
    session = requests.Session()
    vmc_client = create_vmc_client(token, session=session)
    atexit.register(session.close)
    return vmc_client

def list_aws_account(vmc_client, org_id):
    accounts = vmc_client.orgs.account_link.ConnectedAccounts.get(org_id)
    return [
        {
            "text": account.account_number,
            "value": account.id
        } for account in accounts
    ]

def list_region(vmc_client, org_id):
    regions = vmc_client.Orgs.get(org_id).properties.values.get("defaultAwsRegions").split(",")
    return [
        {
            "text": region,
            "value": region
        } for region in regions
    ]

def list_vpc(
    vmc_client, 
    org_id, 
    linked_account_id, 
    region
):
    csbnts = vmc_client.orgs.account_link.CompatibleSubnets.get(
        org_id, 
        linked_account_id=linked_account_id, 
        region=region, 
        sddc=None, 
        force_refresh=None
    )
    vpcs = csbnts.vpc_map.keys()
    return [
        {
            "text": vpc,
            "value": vpc
        } for vpc in vpcs
    ]

def list_subnet(
    vmc_client,
    org_id,
    linked_account_id, 
    region,
    vpc_id
):
    csbnts = vmc_client.orgs.account_link.CompatibleSubnets.get(
        org_id, 
        linked_account_id=linked_account_id, 
        region=region, 
        sddc=None, 
        force_refresh=None
    )
    vpc_subnets = csbnts.get_field("vpc_map").get(vpc_id).subnets
    return [
        {
            "text": "{}, {}".format(sub.subnet_id, sub.name),
            "value": sub.subnet_id
        } for sub in vpc_subnets
    ]

def interactive_handler(event):
    db = dbutils2.DocmentDb(event["db_url"], constant.USER)
    
    user_id = event["user_id"]
    
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    
    result = db.read_event_db(user_id)
    if result is None:
        post_text(event, help_message)
        return
    
    if event["callback_id"] == "create_sddc":
        if event["response"] == "yes":
            post_button(
                event,
                REGION_BUTTON,
#                list_region(
#                    get_vmc_client(event["token"]),
#                    event["org_id"]
#                )
                [
                    {
                        "text": "AP_NORTHEAST_1", #for internal use
                        "value": "AP_NORTHEAST_1" #for internal use
                    }
                ]
            )
            return
        else:
            post_text(
                event,
                "OK, create SDDC has cenceled."
            )
            db.delete_event_db(user_id)
            return
    elif event["callback_id"] == "link_aws_sddc":
        if event["response"] == "yes":
            post_button(
                event,
                ACCOUNT_BUTTON,
#                list_aws_account(
#                    get_vmc_client(event["token"]),
#                    event["org_id"]
#                )
                [
                    {
                        "text": AWS_ACCOUNT, #for internal use
                        "value": AWS_ID #for internal use
                    }
                ]
            )
            db.write_event_db(user_id, {"command": "link_aws", "num_hosts": 1, "link_aws": True})
        else:
            post_text(
                event,
                "Please enter CIDR block for management subnet."
            )
            post_text(
                event,
                "/23 is max 27 hosts, /20 is max 251, /16 is 4091.",
                False
            )
            post_text(
                event,
                "You can not use 10.0.0.0/15 and 172.31.0.0/16 which are reserved.",
                False
            )
            db.write_event_db(user_id, {"command": "link_aws", "num_hosts": 1, "link_aws": False})
    elif event["callback_id"] == "region":
        post_text(
            event,
            "Please enter SDDC name"
        )
        db.write_event_db(user_id, {"command": "region", "region": event["response"]})
    elif event["callback_id"] == "aws_account":
        post_button(
            event,
            VPC_BUTTON,
            list_vpc(
                get_vmc_client(event["token"]),
                event["org_id"],
                event["response"],
                result["region"]
            )
        )
        db.write_event_db(user_id, {"command": "aws_account", "connected_account_id": event["response"]})
    elif event["callback_id"] == "vpc":
        post_button(
            event,
            SUBNET_BUTTON,
            list_subnet(
                get_vmc_client(event["token"]),
                event["org_id"],
                result["connected_account_id"],
                result["region"],
                event["response"]
            )
        )
        db.write_event_db(user_id, {"command": "vpc", "vpc_id": event["response"]})
    elif event["callback_id"] == "subnet":
        post_text(
            event,
            "Please enter CIDR block for management subnet."
        )
        post_text(
            event,
            "/23 is max 27 hosts, /20 is max 251, /16 is 4091.",
            False
        )
        post_text(
            event,
            "You can not use 10.0.0.0/15 and 172.31.0.0/16 which are reserved.",
            False
        )
        db.write_event_db(user_id, {"command": "subnet", "customer_subnet_id": event["response"]})
