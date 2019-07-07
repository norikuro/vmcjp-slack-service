import json
import pymongo
import datetime

from vmcjp.utils import constant

class DocmentDb(object):
    def __init__(self, url): 
        self.client = pymongo.MongoClient(url)
        self.event_db = self.client[constant.USER_DB]
        self.event_col = self.event_db[constant.USER_COLLECTION]
        self.cred_db = self.client[constant.CRED_DB]
        self.cred_col = self.event_db[constant.CRED_COLLECTION]
    
    def get_client(self):
      return self.client

    def get_event_db(self):
        return self.event_db
    
    def get_cred_db(self):
        return self.cred_db

    def get_event_collection(self):
        return self.event_col
    
    def get_cred_collection(self):
        return self.cred_col

    def read_event_db(self, user_id, minutes=None):
        past = (
          datetime.datetime.now() - datetime.timedelta(minutes=minutes)
        ).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        
        if minutes is None:
            cur = self.event_col.find({"_id": user_id})
        else:
            cur = self.event_col.find({"start_time": {"$gt": past}, "_id": user_id})
        
        if cur.count() != 0:
            return cur[0]
        else:
            return
        
    def read_cred_db(self, user_id):
        cur = self.cred_col.find({"_id": user_id})
        if cur.count() != 0:
            return cur[0]
        else:
            return

    def write_event_db(self, user_id, data):
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        data.update({"start_time": now})
        
        self.event_col.update({"_id": user_id}, {"$set": data}, upsert=True)
        
    def write_cred_db(self, user_id, data):
        self.cred_col.update({"_id": user_id}, {"$set": data}, upsert=True)

    def delete_event_db(self, user_id):
        self.event_col.remove({"_id": user_id})
        
    def delete_cred_db(self, user_id):
        self.cred_col.remove({"_id": user_id})
