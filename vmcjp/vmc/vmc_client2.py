import requests
import json

LOGIN_BASE_URL = "https://console.cloud.vmware.com/csp/gateway"
BASE_URL = "https://vmc.vmware.com"
HEADERS = {"Content-Type": "application/json"}

def login(refresh_token):
  uri = "/am/api/auth/api-tokens/authorize"
  params = {"refresh_token": refresh_token}
  
  response = requests.post(
    '{}{}'.format(LOGIN_BASE_URL, uri),
    headers=HEADERS,
    params = params
  )
  
  if response.status_code == 200:
    data = response.json()
    retrun {
      "access_token": data.get("access_token"),
      "expires": data.get("expires_in")
    }
  
