import json
import os
import urllib2
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def post(url, data, bot_oauth_token):
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer {}".format(bot_oauth_token)
    }
    
    request = urllib2.Request(
        url, 
        data=json.dumps(data).encode("utf-8"), 
        headers=headers
    )
    
    return urllib2.urlopen(request)

def post_to_response_url(url, data):
    headers = {
        "Content-Type": "application/json",
    }
    
    request = urllib2.Request(
        url, 
        data=json.dumps(data).encode("utf-8"), 
        headers=headers
    )
    
    return urllib2.urlopen(request)

def post_to_webhook(url, data):
    headers = {
        "Content-Type": "application/json"
    }
    
    request = urllib2.Request(
        url, 
        data=json.dumps(data).encode("utf-8"), 
        headers=headers
    )
    
    return urllib2.urlopen(request)

def post_text(event, text, type="response"):
    logging.info("post_text: " + json.dumps(event) + ",  " + text + ",  " + type)
    data = {
        "token": event["token"],
        "channel": event["channel"],
        "text": text
    }
    logging.info("post_text: " + json.dumps(data))
    
    if "response" in type:
        response = post_to_response_url(event["response_url"], data)
    elif "webhook" in type:
        response = post_to_webhook(event["webhook_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response

def post_option(event, button, option_list):
    logging.info("post_option: " + json.dumps(event) + ",  " + button + ",  " + ",".join(option_list))
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    button_set = json.load(open(button, 'r'))
    button_set["attachments"][0]["actions"][0].update(
        {"options": option_list}
    )
    data.update(button_set)
    logging.info("post_option: " + json.dumps(data))

    return post_to_response_url(event["response_url"], data)

def post_button(event, button, type="response"):
    logging.info("post_button: " + json.dumps(event) + ",  " + button + ",  " + type)
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }

    button_set = json.load(open(button, 'r'))
    data.update(button_set)
    logging.info("post_button: " + json.dumps(data))

    if "response" in type:
        response = post_to_response_url(event["response_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response

def create_button(event, button):
    fields = button.get("attachments")[0].get("fields")
    for field in fields:
        field.update({"value": result.get(field.get("value"))})
    return button

def post_field_button(event, button, pretext=None, type="response"):
    logging.info("post_field_button: " + json.dumps(event) + ",  " + button + ",  " + type)
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    
    button_set = json.load(open(button, 'r'))
    button_set = create_button(event, button_set)
    
    if pretext is not None:
        data.update(
            {"pretext": pretext}
        )
    
    data.update(button_set)
    logging.info("post_field_button: " + json.dumps(data))
    
    if "response" in type:
        response = post_to_response_url(event["response_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response
