import json
import urllib2
import logging

HEADERS = {"Content-Type": "application/json"}

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def post(url, data, bot_oauth_token=None):
    if bot_oauth_token is not None:
        HEADERS.update(
            {
                "Authorization": "Bearer {}".format(
                    bot_oauth_token
                )
            }
        )
    
    request = urllib2.Request(
        url, 
        data=json.dumps(data).encode("utf-8"), 
        headers=HEADERS
    )
    
    return urllib2.urlopen(request)

def post_to_webhook(url, text):
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "text": text
    }
    
    request = urllib2.Request(
        url, 
        data=json.dumps(data).encode("utf-8"), 
        headers=headers
    )
    
    return urllib2.urlopen(request)

def post_text(event, text, type="response"):
    data = {
        "token": event["slack_token"],
        "channel": event["channel"],
        "text": text
    }
    
    if "response" in type:
        response = post(event["response_url"], data)
    elif "webhook" in type:
        response = post(event["webhook_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response

def post_text2(
    url,
    slack_token, 
    channel,
#    text, 
    data,
    bot_token=None
):
    post_data = {
        "token": slack_token,
        "channel": channel,
#        "text": text
    }
    post_data.update(data)
    
    if bot_token is None:
        response = post(url, post_data)
    else:
        response = post(url, post_data, bot_token)
    return response

def post_option(event, button, option_list, type="response"):
#    data = {
#        "token": event["slack_token"],
#        "channel": event["channel"]
#    }
    button_set = json.load(open(button, 'r'))
    button_set["attachments"][0]["actions"][0].update(
        {"options": option_list}
    )
    data.update(button_set)

    if "response" in type:
#        response = post(event["response_url"], data)
        post_text2(
            event["response_url"],
            event["slack_token"],
            event["channel"],
            data
        )
    else:
#        response = post(event["post_url"], data, event["bot_token"])
        post_text2(
            event["post_url"],
            event["slack_token"],
            event["channel"],
            data,
            event["bot_token"]
        )
    return response

def post_button(event, button, type="response"):
    data = {
        "token": event["slack_token"],
        "channel": event["channel"]
    }

    button_set = json.load(open(button, 'r'))
    data.update(button_set)

    if "response" in type:
        response = post(event["response_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response

def create_button(event, button):
    button_set = json.load(open(button, 'r'))
    attachments = button_set.get("attachments")
    for attachment in attachments:
        fields = attachment.get("fields")
#        attachment.update(
#            {
#                "fields": None 
#                if fields is None 
#                else [
#                    {
#                        "value": event.get(field.get("value"))
#                    } 
#                    for field in fields
#                ]
#            }
#        )
        if fields is not None:
            for field in fields:
                field.update({"value": event.get(field.get("value"))})
    return button_set

def post_field_button(event, button, pretext=None, type="response"):
    data = {
        "token": event["slack_token"],
        "channel": event["channel"]
    }
    
    button_set = create_button(event, button)
    
    if pretext is not None:
        data.update(
            {"pretext": pretext}
        )
    
    data.update(button_set)
    
    if "response" in type:
        response = post(event["response_url"], data)
    elif "webhook" in type:
        response = post(event["webhook_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response
