#!/usr/bin/env python

def get_members(obj):
  for x in dir(obj):
    print x, ':', type(eval("obj."+x))

