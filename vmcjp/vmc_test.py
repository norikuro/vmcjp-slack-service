import json
import atexit
import requests

from vmware.vapi.vmc.client import create_vmc_client
from vmcjp.utils.metadata import get_members
from vmcjp.utils.s3utils import read_json_from_s3
from vmcjp.utils import constant

#TEST_ORG_ID = os.environ["test_org"] #for test

class Test(object):
  def get_vmc_client(self, token):
    session = requests.Session()
    vmc_client = create_vmc_client(token, session=session)
    atexit.register(session.close)
    return vmc_client

def main():
  f = json.load(open("vmcjp/s3config.json", 'r'))
  j = read_json_from_s3(f["bucket"], f["config"])
  
  test = Test()
  vmc_client = test.get_vmc_client(j["token"])
  subnets = vmc_client.orgs.account_link.CompatibleSubnets.get(j["org_id"], linked_account_id="e462f412-be3a-3fa4-9d97-59f1217339a6", region="AP_NORTHEAST_1", sddc=None, force_refresh=None)
#  print(get_members(vmc_client.Orgs.get(j["org_id"]).properties))
  print(subnets.vpc_map.keys())
#  print(vmc_client.Orgs.get(j["org_id"]).properties.values.get("defaultAwsRegions").split(","))

if __name__ == '__main__':
  main()
