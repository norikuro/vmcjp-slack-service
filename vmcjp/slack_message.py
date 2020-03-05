import logging

from vmcjp.utils import constant
from vmcjp.utils.slack_post import post_text, post_button, post_option, post_field_button

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

def post_text_(event, text):
    if event.get("response_url") is not None:
        response = post_text_to_response_url(event, text)
    else:
        response = post_text_with_bot_token(event, text)
    return response

def post_option_(event, button, option_list):
    if event.get("response_url") is not None:
        response = post_option_to_response_url(
            event, 
            button, 
            option_list
        )
    else:
        response = post_option_with_bot_token(
            event, 
            button, 
            option_list
        )
    return response

def may_i_message(event):
    text = "May I help you?  Please type `help` if you want to know how to use this Slack App."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def help_message(event):
    help_button = constant.BUTTON_DIR + "help.json"
    response = post_button_with_bot_token(event, help_button)
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
    text = "Please register VMC refesh token at first, type `register org`."
    response = post_text_with_bot_token(event, text)

def register_token_message(event):
    text = "Please enter VMC refresh token."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())
    text = "This conversation will end by typing `cancel`"
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def register_org_message(event):
    text = "Please enter VMC Organization ID."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def delete_org_message(event):
    text = "Deleted VMC Org ID and refresh token from this system db."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def cancel_token_registration_message(event):
    text = "OK, token registration has canceled."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def cancel_org_registration_message(event):
    text = "OK, Org registration has canceled."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def succeed_token_registratuin_message(event):
    text = "Registered VMC refresh token to system db, you can delete it by `delete org`."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def failed_token_registratuin_message(event):
    text = "Failed to register Org ID or token.")
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def succeed_org_registratuin_message(event):
    text = "Registered VMC Org ID to system db."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def wrong_token_message(event):
    text = "You might entered wrong Org ID or token, please check your Org ID or token and enter correct one."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def delete_sddc_message(event):
    delete_button = constant.BUTTON_DIR + "delete.json"
    response = post_option_with_bot_token(
        event, 
        delete_button, 
        event.get("option_list")
    )

def sddc_deletion_confirmation_message(event):
    delete_confirm_button = constant.BUTTON_DIR + "delete_confirm.json"
    response = post_field_button_to_response_url(
        event, 
        delete_confirm_button
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
    response = post_text_(event, text)
#    logging.info(response.read())

def start_create_sddc_wizard_message(event):
    text = "OK, starting create sddc wizard."
    response = post_text_(event, text)
#    logging.info(response.read())
    text = "This conversation will end by typing `cancel` or doing nothing for 5 minutes"
    response = post_text_(event, text)
#    logging.info(response.read())

def check_resources_message(event):
    text = "Checking current resources..."
    response = post_text_(event, text)
#    logging.info(response.read())

def cancel_sddc_creation_message(event):
    text = "OK, canceled a create sddc wizard."
    response = post_text_(event, text)
#    logging.info(response.read())

def no_enough_resouces_message(event):
    text = "Sorry, we don't have enough space to deploy hosts on this org."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())
    text = "Canceled to create sddc."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def max_hosts_message(event):
    precheck_button = constant.BUTTON_DIR + "precheck.json"
    text = "You can deploy max {} hosts.".format(
        event.get("max_hosts")
    )
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())
    response = post_button_with_bot_token(event, precheck_button)
#    logging.info(response.read())

def region_list_message(event):
    region_button = constant.BUTTON_DIR + "region.json"
    response = post_option_(
        event, 
        region_button, 
        event.get("region_list")
    )
#    logging.info(response.read())

def ask_sddc_name_message(event):
    text = "Please enter SDDC name"
    response = post_text_to_response_url(event, text)
#    logging.info(response.read())

def link_aws_message(event):
    link_aws_button = constant.BUTTON_DIR + "link_aws.json"
    if event.get("response_url") is not None:
        response = post_button_to_response_url(event, link_aws_button)
    else:
        response = post_button_with_bot_token(event, link_aws_button)
#    logging.info(response.read())

#def link_aws_single_message(event):
#    link_aws_button = constant.BUTTON_DIR + "link_aws.json"
#    response = post_button_to_response_url(event, link_aws_button)
##    logging.info(response.read())

def single_multi_message(event):
    single_multi_button = constant.BUTTON_DIR + "single_multi.json"
    response = post_button_with_bot_token(event, single_multi_button)
#    logging.info(response.read())

def num_hosts_list(event):
    num_hosts_button = constant.BUTTON_DIR + "num_hosts.json"
    response = post_option_to_response_url(
        event, 
        num_hosts_button, 
        event.get("num_hosts_list")
    )
#    logging.info(response.read())

def aws_account_list_message(event):
    account_button = constant.BUTTON_DIR + "account.json"
    response = post_option_to_response_url(
        event, 
        account_button, 
        event.get("aws_account_list")
    )
#    logging.info(response.read())

def aws_vpc_list_message(event):
    vpc_button = constant.BUTTON_DIR + "vpc.json"
    response = post_option_to_response_url(
        event, 
        vpc_button, 
        event.get("vpc_list")
    )
#    logging.info(response.read())

def aws_subnet_list_message(event):
    subnet_button = constant.BUTTON_DIR + "subnet.json"
    response = post_option_to_response_url(
        event, 
        subnet_button, 
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
    create_button = constant.BUTTON_DIR + "create.json"
    response = post_field_button_with_bot_token(
        event, 
        create_button
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
    list_button = constant.BUTTON_DIR + "list.json"
    response = post_field_button_with_bot_token(
        event, 
        list_button
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
    task_button = constant.BUTTON_DIR + "task.json"
    response = post_field_button_with_bot_token(
        event, 
        task_button
    )
#    logging.info(response.read())
    
def task_webhook_message(event):
    task_button = constant.BUTTON_DIR + "task.json"
    response = post_field_button_to_webhook(
        event, 
        task_button
    )
#    logging.info(response.read())

def start_restore_wizard_message(event):
    text = "OK, start to restore sddc."
    response = post_text_with_bot_token(event, text)
#    logging.info(response.read())

def restore_message(event):
    restore_button = constant.BUTTON_DIR + "restore.json"
    reponse = post_field_button_with_bot_token(
        event, 
        restore_button
    )
#    logging.info(response.read())

def cancel_sddc_restoration_message(event):
    text = "OK, canceled a restore sddc wizard."
    response = post_text_(event, text)
#    logging.info(response.read())

def check_result_message(event):
    response = post_text_to_response_url(
        event, 
        event.get("check_result")
    )
#    logging.info(response.read())
