import datetime

from time import sleep
from vmcjp.utils import dbutils2
from com.vmware.vmc.model_client import Task
from vmcjp.utils.cloudwatch import put_event


def task_handler(task_client, event):
  resp = wait_for_task(task_client, event.get("org_id"), event.get("task_id"))
#  resp = {"status": True, "check_time": 3, "estimated_time": 3}

  db = dbutils2.DocmentDb(event.get("db_url"))
  
  if resp.get("status") == False:
    db.delete_event_db(event.get("user_id"))
    return "{} to {} sddc, {}".format(
      resp.get("message"), 
      event.get("command"), 
      event.get("sddc_name")
    )
  elif resp.get("status") == True and resp.has_key("check_time"):
    event["event_name"] = "{}-{}-{}".format(
      event.get("user_id"),
      event.get("task_id"),
      datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    )
    put_event(resp.get("check_time"), event)
    return "It takes around {} min".format(resp.get("estimated_time"))
  elif resp.get("status") == True:
    db.delete_event_db(event.get("user_id"))
    return "{} successfully to {} sddc, task id: {}".format(
      resp.get("message"), 
      event.get("command"),
      event.get("task_id")
    )

def wait_for_task(task_client, org_id, task_id):
  interval_sec = 60
  
  sleep(30)
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
        else:
          time = 30
        return {
            "status": True, 
            "estimated_time": est_time,
            "check_time": time
        }
      else:
        sleep(interval_sec)
