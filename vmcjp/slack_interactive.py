import json
import logging
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client

from vmcjp.utils import dbutils2
from vmcjp.utils import constant
from vmcjp.utils.lambdautils import call_lambda
from vmcjp import slack_message

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
    if user_name in event.get("user_name"):
        return True
    else:
        return False

def interactive_handler(event):
    user_id = event.get("user_id")
    
    db = dbutils2.DocmentDb(event.get("db_url"))
    result = db.read_event_db(user_id, 5)
    if result is None:
        slack_message.may_i_message(event)
        return

    __cred_data = db.read_cred_db(event.get("user_id"))
    event.update({"token": __cred_data.get("token")})
    if "delete_sddc" in event.get("callback_id"):
        if "delete_sddc" in result.get("status"):
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
            slack_message.sddc_deletion_confirmation_message(event)
    elif "delete_confirmation" in event.get("callback_id"):
        if "yes" in event.get("response"):
            slack_message.started_delete_sddc_message(event)
            event.update(result)
            event.update(
                {"user_name": __cred_data.get("user_name")}
            )
            if check_sddc_user(event):
                call_lambda("delete_sddc", event)
            else:
                slack_message.cannot_delete_sddc_message(event)
                db.delete_event_db(user_id)
        else:
            slack_message.cancel_sddc_deletion_message(event)
            db.delete_event_db(user_id)
        return
    elif "create_sddc" in event.get("callback_id"):
        if "yes" in event.get("response"):
            event.update(
#                {
#                    "region_list": list_region(
#                        get_vmc_client(event.get("token")),
#                        event.get("org_id")
#                    )
#                }
                {
                    "region_list": [
                        {
                            "text": "AP_NORTHEAST_1", #for internal use
                            "value": "AP_NORTHEAST_1" #for internal use
                        }
                    ]
                }
            )
            slack_message.region_list_message(event)
            db.write_event_db(
                event.get("user_id"), 
                {
                    "status": "resource_check"
                }
            ) 
        else:
            slack_message.cancel_sddc_creation_message(event)
            db.delete_event_db(user_id)
        return
    elif "link_aws_sddc" in event.get("callback_id"):
        if "True" in event.get("response"):
            event.update(
                {
#                    "aws_account_list": list_aws_account(
#                        get_vmc_client(event.get("token")),
#                        event.get("org_id")
#                    )
                    "aws_account_list": [
                        {
                            "text": event.get("aws_internal_account"), #for internal use
                            "value": "{}+{}".format(
                                event.get("aws_internal_account"), 
                                event.get("aws_internal_id")
                            ) #for internal use
                        }
                    ]
                }
            )
            slack_message.aws_account_list_message(event)
        else:
            slack_message.ask_cidr_message(event)
        db.write_event_db(
            user_id, 
            {
                "status": "link_aws", 
                "num_hosts": 1, 
                "sddc_type": "1NODE",
                "link_aws": event.get("response")
            }
        )
        return
    elif "region" in event.get("callback_id"):
        slack_message.ask_sddc_name_message(event)
        db.write_event_db(
            user_id, 
            {
                "status": "region", 
                "region": event.get("response")
            }
        )
        return
    elif "single_multi" in event.get("callback_id"):
        if "single" in event.get("response"):
            slack_message.link_aws_single_message(event)
            db.write_event_db(
                user_id,
                {
                    "status": "single_multi"
                }
            )
        else:
            event.update(
                {
                    "num_hosts_list": list_num_hosts(result.get("max_hosts"))
                }
            )
            slack_message.num_hosts_list(event)
            db.write_event_db(
                user_id,
                {
                    "status": "single_multi",
                    "link_aws": "True"
                }
            )
        return
    elif "num_hosts" in event.get("callback_id"):
        event.update(
            {
#                "aws_account_list": list_aws_account(
#                    get_vmc_client(event.get("token")),
#                    event.get("org_id")
#                )
                "aws_account_list": [
                    {
                        "text": event.get("aws_internal_account"), #for internal use
                        "value": "{}+{}".format(
                            event.get("aws_internal_account"), 
                            event.get("aws_internal_id")
                        ) #for internal use
                    }
                ]
            }
        )
        slack_message.aws_account_list_message(event)
        db.write_event_db(
            user_id, 
            {
                "status": "num_hosts",
                "num_hosts": int(event.get("response")), 
                "link_aws": "True"
            }
        )
        return
    elif "aws_account" in event.get("callback_id"):
        aws_account = event.get("response").split("+")[0]
        aws_id = event.get("response").split("+")[1]
        event.update(
            {
                "vpc_list": list_vpc(
                    get_vmc_client(event.get("token")),
                    event.get("org_id"),
                    aws_id,
                    result.get("region")
                )
            }
        )
        slack_message.aws_vpc_list_message(event)
        db.write_event_db(
            user_id, 
            {
                "status": "aws_account", 
                "aws_account": aws_account,
                "connected_account_id": aws_id
            }
        )
        return
    elif "vpc" in event.get("callback_id"):
        event.update(
            {
                "subnet_list": list_subnet(
                    get_vmc_client(event.get("token")),
                    event.get("org_id"),
                    result.get("connected_account_id"),
                    result.get("region"),
                    event.get("response")
                )
            }
        )
        slack_message.aws_subnet_list_message(event)
        db.write_event_db(
            user_id, 
            {
                "status": "vpc", 
                "vpc_id": event.get("response")
            }
        )
        return
    elif "subnet" in event.get("callback_id"):
        slack_message.ask_cidr_message(event)
        db.write_event_db(
            user_id, 
            {
                "status": "subnet", 
                "customer_subnet_id": event.get("response")
            }
        )
        return
    elif "confirmation" in event.get("callback_id"):
        if "yes" in event.get("response"):
            slack_message.start_create_sddc_message(event)
            db.write_event_db(
                user_id, 
                {
                    "status": "creating", 
                }
            )
            event.update(result)
            call_lambda("create_sddc", event)
        else:
            slack_message.cancel_sddc_creation_message(event)
            db.delete_event_db(user_id)
        return
    elif "restore_sddc" in event.get("callback_id"):
        if "yes" in event.get("response"):
            slack_message.check_resources_message(event)
            event.update(result)
#            call_lambda("check_resources", event)
            db.init_sddc_db()
            config = db.get_backedup_sddc_config()
            event.update(config)
            db.write_event_db(event.get("user_id"), config)
#            db.write_event_db(
#                event.get("user_id"), 
#                {
#                    "status": "check_resources"
#                }
#            )
        else:
            slack_message.cancel_sddc_restoration_message(event)
            db.delete_event_db(user_id)
    else:
        return
