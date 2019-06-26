import json
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.metadata import get_members
from vmcjp.utils.s3utils import read_json_from_s3
from vmcjp.utils import constant

#TEST_ORG_ID = os.environ["test_org"] #for test

class Test(object):
  def get_vmc_client(token):
    session = requests.Session()
    vmc_client = create_vmc_client(token, session=session)
    atexit.register(session.close)
    return vmc_client

def main():
  f = json.load(open(constant.S3_CONFIG, 'r'))
  j = read_json_from_s3(f["bucket"], f["config"])
  
  test = Test()
  vmc_client = test.get_vmc_client(j["token"])
  print(get_members(vmc_client.orgs.account_link))
  print(vmc_client.orgs.account_link)

if __name__ == '__main__':
  main()
