import json
import os
import urllib2

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

def post_text(event, text, reply=True):
    data = {
        "token": event["token"],
        "channel": event["channel"],
        "text": text
    }
    
    if reply:
        response = post_to_response_url(event["response_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response

def post_option(event, button, option_list):
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    button_set = json.load(open(button, 'r'))
    button_set["attachments"][0]["actions"][0].update(
        {"options": option_list}
    )
    data.update(button_set)
    return post_to_response_url(event["response_url"], data)

def post_button(event, button, reply=True):
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    button_set = json.load(open(button, 'r'))
    data.update(button_set)
    if reply:
        response = post_to_response_url(event["response_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response

def create_configmation_button(result, button):
    fields = button.get("attachments")[0].get("fields")
    for field in fields:
        field.update({"value": result.get(field.get("value"))})
    return button

def post_confirm_button(event, result, button, reply=True):
    data = {
        "token": event["token"],
        "channel": event["channel"]
    }
    button_set = json.load(open(button, 'r'))
    button_set = create_configmation_button(result, button_set)
    data.update(button_set)
    if reply:
        response = post_to_response_url(event["response_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response
