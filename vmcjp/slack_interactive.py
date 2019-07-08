import json
#import os
import logging
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client

from vmcjp.utils import dbutils2
from vmcjp.utils import constant
from vmcjp.utils.slack_post import post_text, post_option, post_button, post_field_button
from vmcjp.utils.lambdautils import call_lambda

ACCOUNT_BUTTON = constant.BUTTON_DIR + "account.json"
REGION_BUTTON = constant.BUTTON_DIR + "region.json"
VPC_BUTTON = constant.BUTTON_DIR + "vpc.json"
SUBNET_BUTTON = constant.BUTTON_DIR + "subnet.json"
LINK_AWS_BUTTON = constant.BUTTON_DIR + "link_aws.json"
NUM_HOSTS_BUTTON = constant.BUTTON_DIR + "num_hosts.json"
DELETE_CONFIRM_BUTTON = constant.BUTTON_DIR + "delete_confirm.json"

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
        } for sub in vpc_subnets if sub.compatible
    ]

def list_num_hosts(num_hosts):
    return [
        {
            "text": i + 1,
            "value": i + 1
        } for i in range(2, num_hosts)
    ]

def check_sddc_user(event):
    vmc_client = get_vmc_client(event.get("token"))
    sddc = vmc_client.orgs.Sddcs.get(event.get("org_id"), event.get("sddc_id"))
    user_name = sddc.user_name
    logging.info("sddc user name {}, slack user name {}".format(user_name, event.get("user_name")))
    if user_name in event.get("user_name"):
        return True
    else:
        return False

def interactive_handler(event):
    user_id = event.get("user_id")
    
    db = dbutils2.DocmentDb(event.get("db_url"))
    result = db.read_event_db(user_id, 5)
    if result is None:
        response = post_text(event, constant.HELP)
#        logging.info(response.read())
        return

    __cred_data = db.read_cred_db(event.get("user_id"))
    event.update({"token": __cred_data.get("token")})
    if "delete_sddc" in event.get("callback_id"):
        if "delete_sddc" in result.get("command"):
            sddc_name = event.get("response").split("+")[0]
            sddc_id = event.get("response").split("+")[1]
            event.update(
                {"sddc_name": sddc_name}
            )
            db.write_event_db(
                user_id, 
                {
                    "sddc_name": sddc_name,
                    "sddc_id": sddc_id
                }
            )
            post_field_button(
                event, 
                DELETE_CONFIRM_BUTTON, 
                "bot"
            )
    elif "delete_confirmation" in event.get("callback_id"):
        if "yes" in event.get("response"):
            response = post_text(
                event,
                "OK, started to delete sddc!"
            )
#            logging.info(response.read())
            event.update(result)
            event.update(
                {"user_name": __cred_data.get("user_name")}
            )
            if check_sddc_user(event):
                call_lambda("delete_sddc", event)
                db.write_event_db(
                    user_id, 
                    {
                        "command": "delete"
                    }
                )
            else:
                response = post_text(
                    event,
                    "You can delete sddcs which you created only. So canceling to delete sddc."
                )
                db.delete_event_db(user_id)
        else:
            response = post_text(
                event,
                "OK, delete SDDC has cenceled."
            )
#            logging.info(response.read())
            db.delete_event_db(user_id)
        return
    elif "create_sddc" in event.get("callback_id"):
        if "yes" in event.get("response"):
            response = post_option(
                event,
                REGION_BUTTON,
#                list_region(
#                    get_vmc_client(event.get("token")),
#                    event.get("org_id")
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
    elif "link_aws_sddc" in event.get("callback_id"):
        if "True" in event.get("response"):
            response = post_option(
                event,
                ACCOUNT_BUTTON,
#                list_aws_account(
#                    get_vmc_client(event.get("token")),
#                    event.get("org_id")
#                )
                [
                    {
                        "text": event.get("aws_internal_account"), #for internal use
                        "value": "{}+{}".format(
                            event.get("aws_internal_account"), 
                            event.get("aws_internal_id")
                        ) #for internal use
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
                "sddc_type": "1NODE",
                "link_aws": event.get("response")
            }
        )
        return
    elif "region" in event.get("callback_id"):
        response = post_text(
            event,
            "Please enter SDDC name"
        )
#        logging.info(response.read())
        db.write_event_db(
            user_id, 
            {
                "command": "region", 
                "region": event.get("response")
            }
        )
        return
    elif "single_multi" in event.get("callback_id"):
        if "single" in event.get("response"):
            response = post_button(event, LINK_AWS_BUTTON)
#            logging.info(response.read())
            db.write_event_db(
                user_id,
                {
                    "command": "single_multi"
                }
            )
        else:
            response = post_option(
                event, 
                NUM_HOSTS_BUTTON,
                list_num_hosts(result.get("max_hosts"))
            )
#            logging.info(response.read())
            db.write_event_db(
                user_id,
                {
                    "command": "single_multi",
                    "link_aws": "True"
                }
            )
        return
    elif "num_hosts" in event.get("callback_id"):
        response = post_option(
            event,
            ACCOUNT_BUTTON,
#            list_aws_account(
#                get_vmc_client(event.get("token")),
#                event.get("org_id")
#            )
            [
                {
                    "text": event.get("aws_internal_account"), #for internal use
                    "value": "{}+{}".format(
                        event.get("aws_internal_account"), 
                        event.get("aws_internal_id")
                    ) #for internal use
                }
            ]
        )
#        logging.info(response.read())
        db.write_event_db(
            user_id, 
            {
                "command": "num_hosts",
                "num_hosts": int(event.get("response")), 
                "link_aws": "True"
            }
        )
        return
    elif "aws_account" in event.get("callback_id"):
        aws_account = event.get("response").split("+")[0]
        aws_id = event.get("response").split("+")[1]
        response = post_option(
            event,
            VPC_BUTTON,
            list_vpc(
                get_vmc_client(event.get("token")),
                event.get("org_id"),
                aws_id,
                result.get("region")
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
    elif "vpc" in event.get("callback_id"):
        response = post_option(
            event,
            SUBNET_BUTTON,
            list_subnet(
                get_vmc_client(event.get("token")),
                event.get("org_id"),
                result.get("connected_account_id"),
                result.get("region"),
                event.get("response")
            )
        )
#        logging.info(response.read())
        db.write_event_db(
            user_id, 
            {
                "command": "vpc", 
                "vpc_id": event.get("response")
            }
        )
        return
    elif "subnet" in event.get("callback_id"):
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
                "customer_subnet_id": event.get("response")
            }
        )
        return
    elif "confirmation" in event.get("callback_id"):
        if "yes" in event.get("response"):
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
