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
