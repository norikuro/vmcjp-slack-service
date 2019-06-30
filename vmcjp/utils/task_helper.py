import os
import datetime

from time import sleep
from com.vmware.vmc.model_client import Task
from vmcjp.utils.cloudwatch import put_event

TEST_ORG_ID = os.environ["test_org"] #for test

def task_handler(task_client, event):
#  resp = wait_for_task(task_client, event["org_id"], event["task_id"])
#  resp = wait_for_task(task_client, TEST_ORG_ID, event["task_id"]) #for test
  resp = {"status": True, "time": 60} #for test
  
  if resp["status"] == False:
    return "{} to create sddc, {}".format(resp["message"], event["sddc_name"])
  elif resp["status"] == True and resp.has_key("time"):
    event["event_name"] = "{}-{}-{}".format(
      event["user_id"],
      event["task_id"],
      datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    )
#    put_event(resp["time"], event) #for test
    put_event(15, event) #for test
    return "It takes around {} min".format(resp["time"])
  elif resp["status"] == True:
    return "{} successfully to create sddc, task id: {}".format(
      resp["message"], 
      event["task_id"]
    )

def wait_for_task(task_client, org_id, task_id):
  interval_sec = 60
  
  sleep(interval_sec)
  while True:
    task = task_client.get(org_id, task_id)
    
    if task.status == Task.STATUS_FINISHED:
      return {"status": True, "message": "Finished"}
    elif task.status == Task.STATUS_FAILED:
      return {"status": False, "message": "Failed"}
    elif task.status == Task.STATUS_CANCELED:
      return {"status": False, "message": "Canceled"}
    else:
      est_time = task.estimated_remaining_minutes
      if est_time != -1 and est_time > 2:
        if est_time <= 2 and est_time > 10:
          time = 7
        elif est_time <= 10 and est_time > 30:
          time = 20
        elif est_time <= 30 and est_time > 60:
          time = 45
        elif est_time <= 60 and est_time > 120:
          time = 90
        else:
          time = 150
        return {"status": True, "time": time}
      else:
        sleep(interval_sec)
