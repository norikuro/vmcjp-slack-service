import json
import pymongo

class DocmentDb(object):
  def __init__(self, url, db_name):
    self.client = pymongo.MongoClient(url)
    self.db = self.client["{}_db".format(db_name)]
    self.collection = self.db["{}_collection".format(db_name)]
    
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
  
  def find(self, query):
    cur = self.collection.find(query)
    if cur.count() != 0:
      return cur[0]
    else:
      return

  def remove(self, data_to_remove):
    self.collection.remove(data_to_remove)
