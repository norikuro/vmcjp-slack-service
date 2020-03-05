import requests
import logging

BASE_URL = "https://console.cloud.vmware.com/csp/gateway"
#HEADERS = {"Content-Type": "application/json"}
HEADERS = {"application/x-www-form-urlencoded"}

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def login(token, org_id):
#  uri = "/am/api/auth/api-tokens/authorize"
  uri = "/am/api/auth/authorize"
#  payload = {"refresh_token": token}
  payload = {
    "grant_type": "refresh_token",
    "refresh_token": token,
    "orgId": org_id
  }
  
  logging.info("!!!!!next is requests.post")
  response = requests.post(
    '{}{}'.format(BASE_URL, uri), 
    headers=HEADERS, 
    params=payload
  )
  
  return response

def get_username(access_token):
  uri = "/am/api/loggedin/user"
  auth_header = {
      "Content-Type": "application/json", 
      "csp-auth-token": access_token
  }
  
  response = requests.get('{}{}'.format(BASE_URL, uri), headers = auth_header)
  if response.status_code != 200:
    return
  else:
    return response.json().get("username")

def validate_token(token, org_id):
    logging.info("!!!!!next is login")
    response = login(token, org_id)
    logging.info("!!!!!got response")
    logging.info(response)
    logging.info(response.status_code)
    logging.info(response.headers)
    logging.info(response.text)

    if response.status_code == 200:
      return get_username(response.json().get("access_token"))
    elif response.status_code == 400:
      raise Exception("Invalid request body | In case of expired refresh_token.")
    elif response.status_code == 401:
      raise Exception("Unauthorized")
    elif response.status_code == 404:
      raise Exception("Organization not found")
    else:
      raise Exception("Something wrong!")
