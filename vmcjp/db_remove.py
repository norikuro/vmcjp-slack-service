import datetime

from vmcjp.utils import dbutils2

class Test(object):
  def db(self):
    db = dbutils2.DocmentDb("mongodb://master:VMware1!@ip-172-30-20-57.ap-northeast-1.compute.internal:27017/")
#    collection = db.get_cred_collection()
    collection = db.get_event_collection()
    collection.remove()
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
