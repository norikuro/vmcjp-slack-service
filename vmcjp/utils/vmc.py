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
    auth_json = response.json().get("access_token")
    return {
      "Content-Type": "application/json", 
      "csp-auth-token": auth_json
    }

def get_username(auth_header):
  uri = "/am/api/loggedin/user"
  response = requests.get('{}{}'.format(BASE_URL, uri), headers = auth_header)
  if response.status_code != 200:
    return
  else:
    return response.json().get("username")

def validate_token(event):
    response = login(event.get("token"))
    if response is None:
      return
    else:
      return get_username(response)
