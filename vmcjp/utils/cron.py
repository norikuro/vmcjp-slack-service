#!/usr/bin/env python

import datetime

def get_next_time(minutes):
  now = datetime.datetime.now()
  next_time = now + datetime.timedelta(minutes=minutes)
  cron = "cron({} {} {} {} ? {})".format(next_time.minute, next_time.hour, next_time.day, next_time.month, next_time.year)
  return cron
