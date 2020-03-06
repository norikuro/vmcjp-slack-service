import requests
import json
import logging

BASE_URL = "https://console.cloud.vmware.com/csp/gateway"
HEADERS = {"Content-Type": "application/json"}

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def login(token):
  uri = "/am/api/auth/api-tokens/details"
  payload = json.dumps({"tokenValue": token}).encode("utf-8")
  
  response = requests.post(
    '{}{}'.format(BASE_URL, uri), 
    headers=HEADERS, 
    data=payload
  )
  
  return response

def validate_token(token, org_id):
    response = login(token)
    
    logging.info("status code: {}".format(response.status_code))
    logging.info(response.json())
    
    if response.status_code == 200:
      data = response.json()
      if data.get("orgId") == org_id:
        return data.get("username")
