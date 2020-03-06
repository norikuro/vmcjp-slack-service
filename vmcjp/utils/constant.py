#!/usr/bin/env python

import sys

class _const:
  S3_CONFIG = "vmcjp/s3config.json"
#  S3_CONFIG = "vmcjp/test_s3config.json" #for test
  SDDC_DB = "sddc_db"
  SDDC_COLLECTION = "sddc_collection"
  USER_DB = "user_db"
  USER_COLLECTION = "user_collection"
  CRED_DB = "cred_db"
  CRED_COLLECTION = "cred_collection"
  BUTTON_DIR = "vmcjp/slack/button/"
  INT_STATUS = ["create_sddc", "resource_check", "sddc_name", "single_multi", "num_hosts", "aws_account", "vpc", "vpc_cidr", "link_aws"]  
  
  MAY_I = "may_i_message"
  HELP = "help_message"
  ASK_SELECT_BUTTON = "ask_select_button_message"
  ASK_WAIT_TASK = "ask_wait_to_finish_task_message"
  ASK_REGISTER_TOKEN = "ask_register_token_message"
  REGISTER_TOKEN = "register_token_message"
  REGISTER_ORG = "register_org_message"
  DELETE_ORG = "delete_org_message"
  CALCEL_TOKEN = "cancel_token_registration_message"
  CANCEL_PRG = "cancel_org_registration_message"
  SUCCESS_TOKEN = "succeed_token_registration_message"
  FAILED_TOKEN = "failed_token_registration_message"
  WRONG_TOKEN = "wrong_token_message"
  DELETE_SDDC = "delete_sddc_message"
  CONFIRM_DELETE = "sddc_deletion_confirmation_message"
  START_DELETE = "started_delete_sddc_message"

  class ConstError(TypeError):
    pass
  
  def __setattr__(self, name, value):
    if name in self.__dict__:
      raise self.ConstError("Can't rebind const (%s)" % name)
    self.__dict__[name] = value

sys.modules[__name__]=_const()
