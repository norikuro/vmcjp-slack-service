#!/usr/bin/env python

#import pymongo
#import sys

from vmcjp.utils import dbutils

class Test(object):
  def db(self):
    db = dbutils.DocmentDb("vmcjp/s3config.json", "user_db", "user_collection")
    collection = db.get_collection()
#    collection.remove()
    col = collection.find({"insertDate": {"$gt": ISODate("2016-10-22T00:00:00+09:00")}})
    for data in col:
      print(data)
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
