#!/usr/bin/env python

#import pymongo
#import sys

from vmcjp.utils import dbutils

class Test(object):
  def db(self):
    db = dbutils.DocmentDb("vmcjp/s3config.json", "user_db", "user_collection")
    collection = db.get_collection()
#    collection.remove()
    col = collection.find()
    for data in col:
      print(data)
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
