import json
import urllib2
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def post(url, data, bot_oauth_token=None):
    headers = {
        "Content-Type": "application/json"
    }
    
    if bot_oauth_token is not None:
        headers.update(
            {
                "Authorization": "Bearer {}".format(
                    bot_oauth_token
                )
            }
        )
    
    request = urllib2.Request(
        url, 
        data=json.dumps(data).encode("utf-8"), 
        headers=headers
    )
    
    return urllib2.urlopen(request)

#def post_to_webhook(url, text):
#    headers = {
#        "Content-Type": "application/json"
#    }
    
#    data = {
#        "text": text
#    }
    
#    request = urllib2.Request(
#        url, 
#        data=json.dumps(data).encode("utf-8"), 
#        headers=headers
#    )
    
#    return urllib2.urlopen(request)

#def post_text(event, text, type="response"):
#    data = {
#        "token": event["slack_token"],
#        "channel": event["channel"],
#        "text": text
#    }
    
#    if "response" in type:
#        response = post(event["response_url"], data)
#    elif "webhook" in type:
#        response = post(event["webhook_url"], data)
#    else:
#        response = post(event["post_url"], data, event["bot_token"])
#    return response

def post_text2(
    url,
    slack_token, 
    channel,
    data,
    bot_token=None
):
    post_data = {
        "token": slack_token,
        "channel": channel,
    }
    post_data.update(data)
    
#    if bot_token is None:
#        response = post(url, post_data)
#    else:
#        response = post(url, post_data, bot_token)
    response = post(url, post_data, bot_token)
    return response

def post_option2(
    url,
    slack_token, 
    channel,
    button, 
    option_list, 
    bot_token=None
):
    button_set = json.load(open(button, 'r'))
    button_set["attachments"][0]["actions"][0].update(
        {"options": option_list}
    )
    
    if bot_token is None:
        response = post_text2(
            url,
            slack_token,
            channel,
            button_set
        )
    else:
        response = post_text2(
            url,
            slack_token,
            channel,
            button_set,
            bot_token
        )
    return response

#def post_option(event, button, option_list, type="response"):
#    button_set = json.load(open(button, 'r'))
#    button_set["attachments"][0]["actions"][0].update(
#        {"options": option_list}
#    )

#    if "response" in type:
#        response = post_text2(
#            event["response_url"],
#            event["slack_token"],
#            event["channel"],
#            button_set
#        )
#    else:
#        response = post_text2(
#            event["post_url"],
#            event["slack_token"],
#            event["channel"],
#            button_set,
#            event["bot_token"]
#        )
#    return response

def post_button2(
    url, 
    slack_token,
    channel,
    button, 
    bot_token=None
):
    button_set = json.load(open(button, 'r'))

    if bot_token is None:
        response = post_text2(
            url,
            slack_token,
            channel,
            button_set
        )
    else:
        response = post_text2(
            url,
            slack_token,
            channel,
            button_set,
            bot_token
        )
    return response

#def post_button(event, button, type="response"):
#    button_set = json.load(open(button, 'r'))
#
#    if "response" in type:
#        response = post_text2(
#            event["response_url"],
#            event["slack_token"],
#            event["channel"],
#            button_set
#        )
#    else:
#        response = post_text2(
#            event["post_url"],
#            event["slack_token"],
#            event["channel"],
#            button_set,
#            event["bot_token"]
#        )
#    return response

def create_button(field_dics, button):
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
                field.update({"value": field_dics.get(field.get("value"))})
    return button_set

def post_field_button2(
    url, 
    slack_token, 
    channel, 
    button, 
    field_dics, 
#    pretext=None, 
    bot_token=None
):
    button_set = create_button(field_dics, button)
    
#    if pretext is not None:
#        button_set.update(
#            {"pretext": pretext}
#        )
#    button_set.update(button_set)
    
    if bot_token is None:
        response = post_text2(
            url,
            slack_token,
            channel,
            button_set
        )
    else:
        response = post_text2(
            url,
            slack_token,
            channel,
            button_set,
            bot_token
        )
    return response

#def post_field_button(
#    event, 
#    button, 
#    pretext=None, 
#    type="response"
#):
#    button_set = create_button(event, button)
    
#    if pretext is not None:
#        button_set.update(
#            {"pretext": pretext}
#        )
#    button_set.update(button_set)
    
#    if "response" in type:
#        response = post_text2(
#            event["response_url"],
#            event["slack_token"],
#            event["channel"],
#            button_set
#        )
#    elif "webhook" in type:
#        response = post_text2(
#            event["webhook_url"],
#            event["slack_token"],
#            event["channel"],
#            button_set
#        )
#    else:
#        response = post_text2(
#            event["post_url"],
#            event["slack_token"],
#            event["channel"],
#            button_set,
#            event["bot_token"]
#        )
#    return response
