import json
import os
import logging
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client

from vmcjp.utils import dbutils2
from vmcjp.utils import constant
from vmcjp.utils.slack_post import post_text, post_option, post_button
from vmcjp.utils.lambdautils import call_lambda

help_message = "May I help you? please type `help`."

TEST_ORG_ID = os.environ["test_org"] #for test
AWS_ACCOUNT = os.environ["aws_account"] #for internal use
AWS_ID = os.environ["aws_id"] #for internal use
ACCOUNT_BUTTON = constant.BUTTON_DIR + "account_button.json"
REGION_BUTTON = constant.BUTTON_DIR + "region_button.json"
VPC_BUTTON = constant.BUTTON_DIR + "vpc_button.json"
SUBNET_BUTTON = constant.BUTTON_DIR + "subnet_button.json"
LINK_AWS_BUTTON = constant.BUTTON_DIR + "link_aws_button.json"
NUM_HOSTS_BUTTON = constant.BUTTON_DIR + "num_hosts_button.json"

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
            "value": "{}+{}".format(
                account.account_number, 
                account.id)
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

def list_num_hosts(num_hosts):
    return [
        {
            "text": i + 1,
            "value": i + 1
        } for i in range(2, num_hosts)
    ]

def interactive_handler(event):
    user_id = event["user_id"]
    
    db = dbutils2.DocmentDb(event["db_url"], constant.USER)
    result = db.read_event_db(user_id, 5)
    if result is None:
        response = post_text(event, help_message)
#        logging.info(response.read())
        return
    
    if event["callback_id"] == "create_sddc":
        if event["response"] == "yes":
            response = post_option(
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
#            logging.info(response.read())
        else:
            response = post_text(
                event,
                "OK, create SDDC has cenceled."
            )
#            logging.info(response.read())
            db.delete_event_db(user_id)
        return
    elif event["callback_id"] == "link_aws_sddc":
        if event["response"] == "True":
            response = post_option(
                event,
                ACCOUNT_BUTTON,
#                list_aws_account(
#                    get_vmc_client(event["token"]),
#                    event["org_id"]
#                )
                [
                    {
                        "text": AWS_ACCOUNT, #for internal use
                        "value": "{}+{}".format(AWS_ACCOUNT, AWS_ID) #for internal use
                    }
                ]
            )
#            logging.info(response.read())
        else:
            response = post_text(
                event,
                "Please enter CIDR block for management subnet."
            )
#            logging.info(response.read())
            response = post_text(
                event,
                "/23 is max 27 hosts, /20 is max 251, /16 is 4091.",
                "bot"
            )
#            logging.info(response.read())
            response = post_text(
                event,
                "You can not use 10.0.0.0/15 and 172.31.0.0/16 which are reserved.",
                "bot"
            )
#            logging.info(response.read())
        db.write_event_db(
            user_id, 
            {
                "command": "link_aws", 
                "num_hosts": 1, 
                "sddc_type": "1NODE"
            }
        )
        return
    elif event["callback_id"] == "region":
        response = post_text(
            event,
            "Please enter SDDC name"
        )
#        logging.info(response.read())
        db.write_event_db(
            user_id, 
            {
                "command": "region", 
                "region": event["response"]
            }
        )
        return
    elif event["callback_id"] == "single_multi":
        if "single" in event["response"]:
            response = post_button(event, LINK_AWS_BUTTON)
#            logging.info(response.read())
        else:
            response = post_option(
                event, 
                NUM_HOSTS_BUTTON,
                list_num_hosts(result["max_hosts"])
            )
#            logging.info(response.read())
        db.write_event_db(
            user_id,
            {
                "command": "single_multi"
            }
        )
        return
    elif event["callback_id"] == "num_hosts":
        response = post_option(
            event,
            ACCOUNT_BUTTON,
#            list_aws_account(
#                get_vmc_client(event["token"]),
#                event["org_id"]
#            )
            [
                {
                    "text": AWS_ACCOUNT, #for internal use
                    "value": "{}+{}".format(AWS_ACCOUNT, AWS_ID) #for internal use
                }
            ]
        )
#        logging.info(response.read())
        db.write_event_db(
            user_id, 
            {
                "command": "num_hosts",
                "num_hosts": int(event["response"]), 
                "link_aws": "True"
            }
        )
        return
    elif event["callback_id"] == "aws_account":
        aws_account = event["response"].split("+")[0]
        aws_id = event["response"].split("+")[1]
        response = post_option(
            event,
            VPC_BUTTON,
            list_vpc(
                get_vmc_client(event["token"]),
                event["org_id"],
                aws_id,
                result["region"]
            )
        )
#        logging.info(response.read())
        db.write_event_db(
            user_id, 
            {
                "command": "aws_account", 
                "aws_account": aws_account,
                "connected_account_id": aws_id
            }
        )
        return
    elif event["callback_id"] == "vpc":
        response = post_option(
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
#        logging.info(response.read())
        db.write_event_db(
            user_id, 
            {
                "command": "vpc", 
                "vpc_id": event["response"]
            }
        )
        return
    elif event["callback_id"] == "subnet":
        response = post_text(
            event,
            "Please enter CIDR block for management subnet."
        )
#        logging.info(response.read())
        response = post_text(
            event,
            "/23 is max 27 hosts, /20 is max 251, /16 is 4091.",
            "bot"
        )
#        logging.info(response.read())
        response = post_text(
            event,
            "You can not use 10.0.0.0/15 and 172.31.0.0/16 which are reserved.",
            "bot"
        )
#        logging.info(response.read())
        db.write_event_db(
            user_id, 
            {
                "command": "subnet", 
                "customer_subnet_id": event["response"]
            }
        )
        return
    elif event["callback_id"] == "confirmation":
        if event["response"] == "yes":
            response = post_text(
                event,
                "OK, started to create sddc!"
            )
#            logging.info(response.read())
            event.update(result)
            call_lambda("create_sddc", event)
            db.write_event_db(
                user_id, 
                {
                    "command": "create"
                }
            )
        else:
            response = post_text(
                event,
                "OK, create SDDC has cenceled."
            )
#            logging.info(response.read())
            db.delete_event_db(user_id)
        return
    else:
        return
