#!/usr/bin/env python

import sys

class _const:
  COMMAND_ORG = {
    "register org": "register_org",
    "register org id": "register_org_id",
    "delete org": "delete_org",
    "cancel": "cancel"
  }
  
  COMMAND_SDDC = {
    "create sddc": "create_sddc",
    "delete sddc": "delete_sddc",
    "list sddcs": "list_sddcs",
    "restore sddc": "restore_sddc", # for internal use
  }
  
  #followings are status of register ORG and token
  REGISTER_ORG_ID = "register_org_id"
  REGISTER_TOKEN = "register_token"
  REGISTERED = "registered"
  
  #followings are status of create SDDC
  CHECK_MAX_HOSTS = "check_max_hosts"
  AWS_REGION = "aws_region"
  SDDC_NAME = "sddc_name"
  SINGLE_MULTI = "single_multi"
  NUM_HOSTS = "num_hosts"
  AWS_ACCOUNT = "aws_account"
  AWS_VPC = "aws_vpc"
  AWS_SUBNET = "aws_subnet"
  MGMT_CIDR = "mgmt_cidr"
  CHECK_CONFIG = "check_config"
  CREATING = "creating"
  
  #followings are status of delete SDDC
  DELETE_SDDC = "delete_sddc"

  class ConstError(TypeError):
    pass
  
  def __setattr__(self, name, value):
    if name in self.__dict__:
      raise self.ConstError("Can't rebind const (%s)" % name)
    self.__dict__[name] = value

sys.modules[__name__]=_const()
