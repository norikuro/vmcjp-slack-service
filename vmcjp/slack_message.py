from vmcjp.utils.slack_post import post_text, post_button, post_option, post_field_button

def ask_register_token_message(event):
  response = post_text(
    event,
    "Please register VMC reresh token at first, type `register token`.",
    "bot"
  )
#  logging.info(response.read())
