#!/usr/bin/env python

import json
import pymongo

from vmcjp.utils.s3utils import read_json_from_s3, download_from_s3

class DocmentDb(object):
  def __init__(self, s3config, db_name, collection_name):
    f = json.load(open(s3config, 'r'))
    url = read_json_from_s3(f["bucket"], f["config"])["db_url"]

    self.client = pymongo.MongoClient(url)
    self.db = self.client[db_name]
    self.collection = self.db[collection_name]
    
  def get_client(self):
    return self.client
  
  def get_db(self):
    return self.db
  
  def get_collection(self):
    return self.collection
  
  def upsert(self, query, update_data):
    self.collection.update(query, update_data, upsert=True)

  def find_with_fields(self, query, fields):
    return self.collection.find(query, fields)[0]
