import requests
import json
import time

LOGIN_URL = "https://console.cloud.vmware.com/csp/gateway"
VMC_URL = "https://vmc.vmware.com"
HEADERS = {"Content-Type": "application/json"}

def login(refresh_token):
    uri = "/am/api/auth/api-tokens/authorize"
    params = {"refresh_token": refresh_token}
    
    response = requests.post(
        '{}{}'.format(LOGIN_URL, uri),
        headers=HEADERS,
      params = params
    )
    now = time.time()
    
    if response is not None:
        status_code = response.status_code
        data = response.json()
        if status_code == 200:
            return {
                "access_token": data.get("access_token"),
                "expire_time": now + data.get("expires_in")
            }
        else:
            return data

def list_sddcs(access_token, org_id):
    uri = "/orgs/{}/sddcs".format(org_id)
    headers = {"csp-auth-token": access_token}
    headers.update(HEADERS)
    
    response = requests.get(
        '{}{}'.format(VMC_URL, uri),
        headers=headers
    )
