import logging

from vmcjp.utils import constant
from vmcjp.utils.slack_post import post_text, post_button, post_option, post_field_button

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
SUBNET_BUTTON = constant.BUTTON_DIR + "subnet.json"
TASK_BUTTON = constant.BUTTON_DIR + "task.json"
RESTORE_BUTTON = constant.BUTTON_DIR + "restore.json"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def post_text_with_bot_token(event, text):
    data = {"text": text}
    response = post_text(
        event.get("post_url"),
        event.get("slack_token"),
        event.get("channel"),
        data,
        event.get("bot_token")
    )
    return response

def post_text_to_response_url(event, text):
    data = {"text": text}
    response = post_text(
        event.get("response_url"),
        event.get("slack_token"),
        event.get("channel"),
        data
    )
    return response

def post_text_to_webhook(event, text):
    data = {"text": text}
    response = post_text(
        event.get("webhook_url"),
        event.get("slack_token"),
        event.get("channel"),
        data
    )
    return response

def post_option_with_bot_token(event, button, option_list):
    response = post_option(
        event.get("post_url"),
        event.get("slack_token"), 
        event.get("channel"),
        button, 
        option_list, 
        event.get("bot_token")
    )
    return response

def post_option_to_response_url(event, button, option_list):
    response = post_option(
        event.get("response_url"),
        event.get("slack_token"), 
        event.get("channel"),
        button, 
        option_list
    )
    return response

def post_button_to_response_url(event, button):
    response = post_button(
        event.get("response_url"),
        event.get("slack_token"), 
        event.get("channel"),
        button
    )
    return response

def post_button_with_bot_token(event, button):
    response = post_button(
        event.get("post_url"),
        event.get("slack_token"), 
        event.get("channel"),
        button,
        event.get("bot_token")
    )
    return response

def post_field_button_to_response_url(event, button):
    response = post_field_button(
        event.get("response_url"),
        event.get("slack_token"), 
        event.get("channel"),
        button,
        event
    )

def post_field_button_to_webhook(event, button):
    response = post_field_button(
        event.get("webhook_url"),
        event.get("slack_token"), 
        event.get("channel"),
        button,
        event
    )

def post_field_button_with_bot_token(event, button):
    response = post_field_button(
        event.get("post_url"),
        event.get("slack_token"), 
        event.get("channel"),
        button,
        event,
        event.get("bot_token")
    )

def may_i_message(event):
    text = "May I help you?  Please type `help` if you want to know how to use this Slack App."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def help_message(event):
    response = post_button_with_bot_token(event, HELP_BUTTON)
#    logging.info(response.read())

def ask_select_button_message(event):
    text = "Please select appropriate button above."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def ask_wait_to_finish_task_message(event):
    text = "Creating sddc now, please wait until the task is finished."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def ask_register_token_message(event):
    text = "Please register VMC reresh token at first, type `register token`."
    response = post_text_with_bot_token(event, text)

def register_token_message(event):
    text = "Please enter VMC refresh token."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def delete_token_message(event):
    text = "Deleted VMC refresh token from system db."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def cancel_token_registration_message(event):
    text = "OK, token registration has canceled."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def succeed_token_registratuin_message(event):
    text = "Registered VMC refresh token to system db, you can delete it with `delete token`."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def wrong_token_message(event):
    text = "Token number you entered is something wrong, please check your token and enter correct token."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def delete_sddc_message(event):
    response = post_option_with_bot_token(
        event, 
        DELETE_BUTTON, 
        event.get("option_list")
    )

def sddc_deletion_confirmation_message(event):
    response = post_field_button_to_response_url(
        event, 
        DELETE_CONFIRM_BUTTON
    )
#    logging.info(response.read())

def started_delete_sddc_message(event):
    text = "OK, started to delete sddc!"
    response = post_text_to_response_url(event, text)
#    logging.info(response.read())

def cannot_delete_sddc_message(event):
    text = "You cannot delete this sddc because the owner is someone else.  You can delete sddcs which you created only.  So canceling this delete task."
    response = post_text_to_response_url(event, text)
#    logging.info(response.read())

def cancel_sddc_deletion_message(event):
    text = "OK, delete SDDC has cenceled."
    if event.get("response_url") is not None:
        response = post_text_to_response_url(event, text)
    else:
        response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def start_create_sddc_wizard_message(event):
    text = "OK, starting create sddc wizard."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())
    text = "This conversation will end by typing `cancel` or doing nothing for 5 minutes"
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())
    text = "Checking current resources..."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def cancel_sddc_creation_message(event):
    text = "OK, canceled a create sddc wizard."
    if event.get("response_url") is not None:
        response = post_text_to_response_url(event, text)
    else:
        response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def no_enough_resouces_message(event):
    text = "Sorry, we don't have enough space to deploy hosts on this org."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())
    text = "Canceled to create sddc."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def max_hosts_message(event):
    text = "You can deploy max {} hosts.".format(
        event.get("max_hosts")
    )
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())
    response = post_button_with_bot_token(event, PRECHECK_BUTTON)
#    logging.info(response.read())

def region_list_message(event):
    response = post_option_to_response_url(
        event, 
        REGION_BUTTON, 
        event.get("region_list")
    )
#    logging.info(response.read())

def ask_sddc_name_message(event):
    text = "Please enter SDDC name"
    response = post_text_to_response_url(event, text)
#    logging.info(response.read())

def link_aws_message(event):
    response = post_button_with_bot_token(event, LINK_AWS_BUTTON)
#    logging.info(response.read())

def link_aws_single_message(event):
    response = post_button_to_response_url(event, LINK_AWS_BUTTON)
#    logging.info(response.read())

def single_multi_message(event):
    response = post_button_with_bot_token(event, SINGLE_MULTI_BUTTON)
#    logging.info(response.read())

def num_hosts_list(event):
    response = post_option_to_response_url(
        event, 
        NUM_HOSTS_BUTTON, 
        event.get("num_hosts_list")
    )
#    logging.info(response.read())

def aws_account_list_message(event):
    response = post_option_to_response_url(
        event, 
        ACCOUNT_BUTTON, 
        event.get("aws_account_list")
    )
#    logging.info(response.read())

def aws_vpc_list_message(event):
    response = post_option_to_response_url(
        event, 
        VPC_BUTTON, 
        event.get("vpc_list")
    )
#    logging.info(response.read())

def aws_subnet_list_message(event):
    response = post_option_to_response_url(
        event, 
        SUBNET_BUTTON, 
        event.get("subnet_list")
    )
#    logging.info(response.read())

def ask_cidr_message(event):
    text = "Please enter CIDR block for management subnet."
    response = post_text_to_response_url(event, text)
#    logging.info(response.read())
    text = "/23 is max 27 hosts, /20 is max 251, /16 is 4091."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())
    text = "You can not use 10.0.0.0/15 and 172.31.0.0/16 which are reserved."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def wrong_network_message(event):
    text = "Please enter correct network cidr block."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def create_sddc_confirmation_message(event):
    response = post_field_button_with_bot_token(
        event, 
        CREATE_BUTTON
    )
#    logging.info(response.read())

def start_create_sddc_message(event):
    text = "OK, started to create sddc!"
    response = post_text_to_response_url(event, text)
#    logging.info(response.read())

def list_sddcs_text_message(event):
    text = "Here is SDDCs list in this org."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def list_sddcs_message(event):
    response = post_field_button_with_bot_token(
        event, 
        LIST_BUTTON
    )
#    logging.info(response.read())

def crud_sddc_result_message(event):
    response = post_text_with_bot_token(event, event.get("message"))
#    logging.info(response.read())

def check_task_message(event):
    response = post_text_with_bot_token(event, event.get("status"))
#    logging.info(response.read())

def check_task_webhook_message(event):
    response = post_text_to_webhook(event, event.get("status"))
#    logging.info(response.read())

def started_crud_sddc_message(event):
    text = "Hi <@{}>, started to {} sddc.".format(
        event.get("user_id"),
        event.get("command")
    )
    response = post_text_to_webhook(event, text)
#    logging.info(response.read())

def task_message(event):
    response = post_field_button_with_bot_token(
        event, 
        TASK_BUTTON
    )
#    logging.info(response.read())
    
def task_webhook_message(event):
    response = post_field_button_to_webhook(
        event, 
        TASK_BUTTON
    )
#    logging.info(response.read())

def start_restore_wizard_message(event):
    text = "OK, start to restore sddc."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def restore_message(event):
    reponse = post_field_button_with_bot_token(
        event, 
        RESTORE_BUTTON
    )
#    logging.info(response.read())

def check_resources_message(event):
    text = "OK, checking current VMC resources."
    response = post_text_to_response_url(event, text)
#    logging.info(response.read())

def cancel_sddc_restoration_message(event):
    text = "OK, canceled a restore sddc wizard."
    response = post_text_to_response_url(event, text)
#    logging.info(response.read())

def check_result_message(event):
    response = post_text_to_response_url(
        event, 
        event.get("check_result")
    )
#    logging.info(response.read())
