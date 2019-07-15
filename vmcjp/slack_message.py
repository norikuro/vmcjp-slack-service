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
        "Canceled to register VMC refresh token.",
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

def link_aws_message(event):
    response = post_button(event, LINK_AWS_BUTTON, "bot")
#    logging.info(response.read())

def single_multi_message(event):
    response = post_button(event, SINGLE_MULTI_BUTTON, "bot")
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
