import datetime

from vmcjp.utils import dbutils2

class Test(object):
  def db(self):
    db = dbutils2.DocmentDb("mongodb://master:VMware1!@ip-172-30-20-57.ap-northeast-1.compute.internal:27017/")
    event_col = db.get_event_collection()
    cred_col = db.get_cred_collection()
#    collection.remove()
#    delta = datetime.datetime.now() - datetime.timedelta(minutes=5)
#    past = delta.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
#    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
#    print(past)
#    col = collection.find({"start_time": {"$gt": past}})
#    data = cred_col.find()
#    cur = cred_col.find()
    cur = event_col.find()
#    print(col.count())
    for data in cur:
      print(data)
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
