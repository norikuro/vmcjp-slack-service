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
#  logging.info(response.read())

def ask_register_token_message(event):
  response = post_text(
    event,
    "Please register VMC reresh token at first, type `register token`.",
    "bot"
  )
#  logging.info(response.read())
