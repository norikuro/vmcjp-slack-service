import os
import datetime

from time import sleep
from com.vmware.vmc.model_client import Task
from vmcjp.utils.cloudwatch import put_event

TEST_ORG_ID = os.environ["test_org"] #for test

def task_handler(task_client, event):
  resp = wait_for_task(task_client, event.get("org_id"), event.get("task_id"))
#  resp = wait_for_task(task_client, TEST_ORG_ID, event["task_id"]) #for test
#  resp = {"status": True, "time": 60} #for test
  
  if resp.get("status") == False:
    return "{} to {} sddc, {}".format(
      resp.get("message"), 
      event.get("command"), 
      event("sddc_name")
    )
  elif resp.get("status") == True and resp.has_key("time"):
    event["event_name"] = "{}-{}-{}".format(
      event.get("user_id"),
      event.get("task_id"),
      datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    )
    put_event(resp.get("time"), event) #for test
#    put_event(15, event) #for test
    return "It takes around {} min".format(resp["time"])
  elif resp.get("status") == True:
    return "{} successfully to {} sddc, task id: {}".format(
      resp.get("message"), 
      event.get("command"),
      event.get("task_id")
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
        else:
          time = 30
        return {"status": True, "time": time}
      else:
        sleep(interval_sec)
