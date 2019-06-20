import json
import os
import urllib2

#from urlparse import parse_qs

BOT_OAUTH_TOKEN = os.environ["bot_token"]

def post(url, data):
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer {}".format(BOT_OAUTH_TOKEN)
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
