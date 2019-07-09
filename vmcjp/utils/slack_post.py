import json
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
        response = post_to_response_url(event["response_url"], data)
    elif "webhook" in type:
        response = post_to_webhook(event["webhook_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response

def post_option(event, button, option_list, type="response"):
    data = {
        "token": event["slack_token"],
        "channel": event["channel"]
    }
    button_set = json.load(open(button, 'r'))
    button_set["attachments"][0]["actions"][0].update(
        {"options": option_list}
    )
    data.update(button_set)

    if "response" in type:
        response = post_to_response_url(event["response_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response

def post_button(event, button, type="response"):
    data = {
        "token": event["slack_token"],
        "channel": event["channel"]
    }

    button_set = json.load(open(button, 'r'))
    data.update(button_set)

    if "response" in type:
        response = post_to_response_url(event["response_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response

def create_button(event, button):
    fields = button.get("attachments")[0].get("fields")
    for field in fields:
        field.update({"value": event.get(field.get("value"))})
    return button

def post_field_button(event, button, pretext=None, type="response"):
    data = {
        "token": event["slack_token"],
        "channel": event["channel"]
    }
    
    button_set = json.load(open(button, 'r'))
    button_set = create_button(event, button_set)
    
    if pretext is not None:
        data.update(
            {"pretext": pretext}
        )
    
    data.update(button_set)
    
    if "response" in type:
        response = post_to_response_url(event["response_url"], data)
    elif "webhook" in type:
        response = post_to_response_url(event["webhook_url"], data)
    else:
        response = post(event["post_url"], data, event["bot_token"])
    return response
