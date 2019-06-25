#!/usr/bin/env python

import sys

class _const:
  #S3_CONFIG = "vmcjp/s3config.json"
  S3_CONFIG = "vmcjp/test_s3config.json" #for test
  SDDC_DB = "sddc_db"
  SDDC_COLLECTION = "sddc_collection"
  USER_DB = "user_db"
  USER_COLLECTION = "user_collection"
  SDDC = "sddc"
  USER = "user"
  BUTTON_DIR = "vmcjp/button/"
  

  class ConstError(TypeError):
    pass
  
  def __setattr__(self, name, value):
    if name in self.__dict__:
      raise self.ConstError("Can't rebind const (%s)" % name)
    self.__dict__[name] = value

sys.modules[__name__]=_const()
