import logging

from vmcjp.utils import constant
from vmcjp.utils.slack_post import post_text, post_button, post_option, post_field_button

logger = logging.getLogger()
logger.setLevel(logging.INFO)

PRECHECK_BUTTON = constant.BUTTON_DIR + "precheck.json"
DELETE_BUTTON = constant.BUTTON_DIR + "delete.json"
LIST_BUTTON = constant.BUTTON_DIR + "list.json"
HELP_BUTTON = constant.BUTTON_DIR + "help.json"
LINK_AWS_BUTTON = constant.BUTTON_DIR + "link_aws.json"
SINGLE_MULTI_BUTTON = constant.BUTTON_DIR + "single_multi.json"
CREATE_BUTTON = constant.BUTTON_DIR + "create.json"
DELETE_CONFIRM_BUTTON = constant.BUTTON_DIR + "delete_confirm.json"
REGION_BUTTON = constant.BUTTON_DIR + "region.json"
ACCOUNT_BUTTON = constant.BUTTON_DIR + "account.json"
NUM_HOSTS_BUTTON = constant.BUTTON_DIR + "num_hosts.json"
VPC_BUTTON = constant.BUTTON_DIR + "vpc.json"

def help_message(event):
    response = post_button(event, HELP_BUTTON, "bot")
#    logging.info(response.read())

def ask_wait_to_finish_task_message(event):
    response = post_text( 
        event,
        "Creating sddc now, please wait until the task is finished.",
        "bot"
    )
#    logging.info(response.read())

def ask_register_token_message(event):
    response = post_text(
        event,
        "Please register VMC reresh token at first, type `register token`.",
        "bot"
    )
#    logging.info(response.read())

def register_token_message(event):
    response = post_text(
        event,
        "Please enter VMC refresh token.",
        "bot"
    )
#    logging.info(response.read())

def delete_token_message(event):
    response = post_text(
        event,
        "Deleted VMC refresh token from system db.",
        "bot"
    )
#    logging.info(response.read())

def cancel_token_registration_message(event):
    response = post_text(
        event,
        "OK, token registration has canceled.",
        "bot"
    )
#    logging.info(response.read())

def succeed_token_registratuin_message(event):
    response = post_text(
        event,
        "Registered VMC refresh token to system db, you can delete it with `delete token`.",
        "bot"
    )
#    logging.info(response.read())

def wrong_token_message(event):
    response = post_text(
        event,
        "Token number you entered is something wrong, please check your token and enter correct token.",
        "bot"
    )
#    logging.info(response.read())

def delete_sddc_message(event):
    response = post_option(
        event,
        DELETE_BUTTON,
        event.get("option_list"),
        "bot"
    )
#    logging.info(response.read())

def sddc_deletion_confirmation_message(event):
    response = post_field_button(
        event, 
        DELETE_CONFIRM_BUTTON,
        "bot"
    )
#    logging.info(response.read())

def started_delete_sddc_message(event):
    response = post_text(
        event,
        "OK, started to delete sddc!"
    )
#    logging.info(response.read())

def cannot_delete_sddc_message(event):
    response = post_text(
        event,
        "You cannot delete this sddc because the owner is someone else.  You can delete sddcs which you created only.  So canceling this delete task."
    )
#    logging.info(response.read())

def cancel_sddc_deletion_message(event):
    response = post_text(
        event,
        "OK, delete SDDC has cenceled."
    )
#    logging.info(response.read())

def start_create_sddc_wizard_message(event):
    response = post_text(
        event,
        "OK, starting create sddc wizard.",
        "bot"
    )
#    logging.info(response.read())
    response = post_text(
        event, 
        "This conversation will end by typing `cancel` or doing nothing for 5 minutes", 
        "bot"
    )
#    logging.info(response.read())
    response = post_text(
        event,
        "Checking current resources...",
        "bot"
    )
#    logging.info(response.read())

def cancel_sddc_creation_message(event):
    response = post_text(
        event,
        "OK, canceled a create sddc wizard.",
        "bot"
    )
#    logging.info(response.read())

def no_enough_resouces_message(event):
    response = post_text(
        event,
        "Sorry, we don't have enough space to deploy hosts on this org.",
        "bot"
    )
#    logging.info(response.read())
    response = post_text(
        event,
        "Canceled to create sddc.",
        "bot"
    )
#    logging.info(response.read())

def max_hosts_message(event):
    response = post_text(
        event,
        "You can deploy max {} hosts.".format(
            event.get("max_hosts")
        ),
        "bot"
    )
#    logging.info(response.read())
    response = post_button(event, PRECHECK_BUTTON, "bot")
#    logging.info(response.read())

def region_list_message(event):
    response = post_option(
        event,
        REGION_BUTTON,
        event.get("region_list")
    )
#    logging.info(response.read())

def ask_sddc_name_message(event):
    response = post_text(
        event,
        "Please enter SDDC name"
    )
#    logging.info(response.read())

def link_aws_message(event):
    response = post_button(event, LINK_AWS_BUTTON, "bot")
#    logging.info(response.read())

def link_aws_single_message(event):
    response = post_button(event, LINK_AWS_BUTTON)
#    logging.info(response.read())

def single_multi_message(event):
    response = post_button(event, SINGLE_MULTI_BUTTON, "bot")
#    logging.info(response.read())

def num_hosts_list(event):
    response = post_option(
        event, 
        NUM_HOSTS_BUTTON,
        event.get("num_hosts_list")
    )
#    logging.info(response.read())

def aws_account_list_message(event):
    response = post_option(
        event,
        ACCOUNT_BUTTON,
        event.get("aws_account_list")
    )
#    logging.info(response.read())

def aws_vpc_list_message(event):
    response = post_option(
        event,
        VPC_BUTTON,
        event.get("vpc_list")
    )
#    logging.info(response.read())

def aws_subnet_list_message(event):
    response = post_option(
        event,
        SUBNET_BUTTON,
        subnet_list
    )
#    logging.info(response.read())

def ask_cidr_message(event):
    response = post_text(
        event,
        "Please enter CIDR block for management subnet."
    )
#    logging.info(response.read())
    response = post_text(
        event,
        "/23 is max 27 hosts, /20 is max 251, /16 is 4091.",
        "bot"
    )
#    logging.info(response.read())
    response = post_text(
        event,
        "You can not use 10.0.0.0/15 and 172.31.0.0/16 which are reserved.",
        "bot"
    )
#    logging.info(response.read())

def wrong_network_message(event):
    response = post_text(
        event,
        "Please enter correct network cidr block.",
        "bot"
    )
#    logging.info(response.read())

def create_sddc_confirmation_message(event):
    response = post_field_button(
        event, 
        CREATE_BUTTON, 
        type="bot"
    )
#    logging.info(response.read())

def list_sddcs_text_message(event):
    response = post_text(
        event,
        "Here is SDDCs list in this org.",
        "bot"
    )
#    logging.info(response.read())

def list_sddcs_message(event):
    response = post_field_button(
        event, 
        LIST_BUTTON, 
        type="bot"
    )
#    logging.info(response.read())
