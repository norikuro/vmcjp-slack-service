import datetime

from vmcjp.utils import dbutils

class Test(object):
  def db(self):
    db = dbutils.DocmentDb("vmcjp/s3config.json", "user_db", "user_collection")
    collection = db.get_collection()
#    collection.remove()
#    delta = datetime.datetime.now() - datetime.timedelta(minutes=5)
#    past = delta.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
#    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
#    print(past)
#    col = collection.find({"start_time": {"$gt": past}})
    col = collection.find()
#    print(col.count())
    for data in col:
      print(data)
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
