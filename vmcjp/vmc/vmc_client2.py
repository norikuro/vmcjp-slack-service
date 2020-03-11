import requests
import json
import time

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
    now = time.time()
    
    if response is not None:
        status_code = response.status_code
        data = response.json()
        if status_code == 200:
            expire_in = data.get("expires_in")
            return {
                "access_token": data.get("access_token"),
                "expires_in": expire_in,
                "expire_time": now + expire_in
            }
        elif status_code in [400, 401, 403, 500]:
            message = {
                "status_code": status_code,
                "message": data.get("message")
            }
            raise Exception(message)
    else:
        raise Exception("Cannot connect VMC, Something wrong!")
