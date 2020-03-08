import json

from vmware.vapi.vmc.client import create_vmc_client

from vmcjp.utils import dbutils
from vmcjp.utils import constant
from vmcjp.utils.lambdautils import call_lambda
from vmcjp.slack.messages import message_handler
from vmcjp.vmc.vmc_client import get_vmc_client, list_region, list_aws_account, list_vpc, list_subnet

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)

#def list_subnet(
#    vmc_client,
#    org_id,
#    linked_account_id, 
#    region,
#    vpc_id
#):
#    csbnts = vmc_client.orgs.account_link.CompatibleSubnets.get(
#        org_id, 
#        linked_account_id=linked_account_id, 
#        region=region, 
#        sddc=None, 
#        force_refresh=None
#    )
#    vpc_subnets = csbnts.get_field("vpc_map").get(vpc_id).subnets
#    return [
#        {
#            "text": "{}, {}".format(sub.subnet_id, sub.name),
#            "value": sub.subnet_id
#        } for sub in vpc_subnets if sub.compatible
#    ]

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
    
    db = dbutils.DocmentDb(event.get("db_url"))
    result = db.read_event_db(user_id, 5)
    if result is None:
        message_handler(constant.MAY_I, event)
        return

    __cred_data = db.read_cred_db(event.get("user_id"))
    event.update(
        {
            "token": __cred_data.get("token"),
            "org_id": __cred_data.get("org_id")
        }
    )
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
            message_handler(constant.CONFIRM_DELETE, event)
        return
    elif "delete_confirmation" in event.get("callback_id"):
        if "yes" in event.get("response"):
            message_handler(constant.START_DELETE, event)
            event.update(result)
            event.update(
                {"user_name": __cred_data.get("user_name")}
            )
            if check_sddc_user(event):
                call_lambda("delete_sddc", event)
            else:
                message_handler(constant.CANT_DELETE, event)
                db.delete_event_db(user_id)
        else:
            message_handler(constant.CANCEL_DELETE, event)
            db.delete_event_db(user_id)
        return
    elif "create_sddc" in event.get("callback_id"):
        if "yes" in event.get("response"):
            event.update(
#                {
#                    "region_list": list_region(
#                        event.get("token"),
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
            message_handler(constant.REGION, event)
            db.write_event_db(
                event.get("user_id"), 
                {
                    "status": "resource_check"
                }
            ) 
        else:
            message_handler(constant.CANCEL_SDDC, event)
            db.delete_event_db(user_id)
        return
    elif "link_aws_sddc" in event.get("callback_id"):
        if "True" in event.get("response"):
            event.update(
                {
#                    "aws_account_list": list_aws_account(
#                        event.get("token"),
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
            message_handler(constant.AWS_ACCOUNT, event)
        else:
            message_handler(constant.CIDR, event)
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
        message_handler(constant.SDDC_NAME, event)
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
            message_handler(constant.LINK_AWS, event)
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
            message_handler(constant.NUM_HOSTS, event)
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
#                    event.get("token"),
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
        message_handler(constant.AWS_ACCOUNT, event)
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
                    event.get("token"),
                    event.get("org_id"),
                    aws_id,
                    result.get("region")
                )
            }
        )
        message_handler(constant.AWS_VPC, event)
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
        message_handler(constant.AWS_SUBNET, event)
        db.write_event_db(
            user_id, 
            {
                "status": "vpc", 
                "vpc_id": event.get("response")
            }
        )
        return
    elif "subnet" in event.get("callback_id"):
        message_handler(constant.CIDR, event)
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
            message_handler(constant.CREATE, event)
            db.write_event_db(
                user_id, 
                {
                    "status": "creating", 
                }
            )
            event.update(result)
            call_lambda("create_sddc", event)
        else:
            message_handler(constant.CANCEL_SDDC, event)
            db.delete_event_db(user_id)
        return
    elif "restore_sddc" in event.get("callback_id"):
        if "yes" in event.get("response"):
            message_handler(constant.CHECK_RESOURCE, event)
            event.update(result)
            call_lambda("check_resources", event)
            db.write_event_db(
                event.get("user_id"), 
                {
                    "status": "check_resources"
                }
            )
        else:
            message_handler(constant.CANCEL_RESTORE, event)
            db.delete_event_db(user_id)
        return
    else:
        return
