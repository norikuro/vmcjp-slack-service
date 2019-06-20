from time import sleep

from com.vmware.vmc.model_client import Task

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
