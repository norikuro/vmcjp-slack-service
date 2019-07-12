import logging

from vmcjp.utils.slack_post import post_text, post_button, post_option, post_field_button

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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

    def no_enough_resouces_message(event):
        response = post_text(
            event,
            "Sorry, we don't have enough space to deploy hosts on this org.",
            "bot"
        )
#        logging.info(response.read())
        response = post_text(
            event,
            "Canceled to create sddc.",
            "bot"
        )
#        logging.info(response.read())
