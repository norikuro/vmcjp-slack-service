import requests

BASE_URL = "https://console.cloud.vmware.com/csp/gateway"
HEADERS = {"Content-Type": "application/json"}

def login(token):
  uri = "/am/api/auth/api-tokens/authorize"
  payload = {"refresh_token": token}
  response = requests.post(
    '{}{}'.format(BASE_URL, uri), 
    headers=HEADERS, 
    params=payload
  )
  
  if response.status_code != 200:
    return
  else:
    access_token = response.json().get("access_token")
    return access_token

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

def validate_token(token):
    response = login(token)
    
    if response is None:
      return
    else:
      return get_username(response)
