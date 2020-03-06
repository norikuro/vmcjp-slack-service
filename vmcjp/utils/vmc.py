import requests
import json

BASE_URL = "https://console.cloud.vmware.com/csp/gateway"
HEADERS = {"Content-Type": "application/json"}


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
    
    if response.status_code == 200:
      data = response.json()
      if data.get("OrgID") == org_id:
        return data.get("username")
