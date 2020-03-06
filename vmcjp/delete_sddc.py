#import logging
import requests
import atexit

from vmware.vapi.vmc.client import create_vmc_client
from com.vmware.vmc.model_client import ErrorResponse
from com.vmware.vapi.std.errors_client import InvalidRequest

from vmcjp.utils.task_helper import task_handler
from vmcjp.utils.lambdautils import call_lambda
from vmcjp.utils import constant
from vmcjp.slack.messages import message_handler

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)

def get_vmc_client(token):  
  session = requests.Session()
  vmc_client = create_vmc_client(token, session=session)
  atexit.register(session.close)
  return vmc_client

def delete_sddc(
  org_id,
  sddc_id,
  vmc_client
):

  try:
    task = vmc_client.orgs.Sddcs.delete(
      org=org_id, 
      sddc=sddc_id
    )
  except InvalidRequest as err:
    error_response = err.data.convert_to(ErrorResponse)
    messages = error_response.error_messages
    message = None if len(messages) <= 0 else messages[0]
    raise Exception(message)
  return task.id

def lambda_handler(event, context):
#  logging.info(event)
  event.update({"lambda_name": "check_task"})
  
  vmc_client = get_vmc_client(event.get("token"))
  try:
    task_id = delete_sddc(
      event.get("org_id"),
      event.get("sddc_id"),
      vmc_client
    )
    event.update({"task_id": task_id})
  except Exception as e:
    event.update(
      {
        "message": "Sorry, failed to delete sddc.  {}".format(e.message),
        "status": "task_failed"
      }
    )
    message_handler(constant.SDDC_RESULT, event)
    call_lambda("check_task", event)
    return 
  
  message_handler(constant.TASK_MSG, event)
  message_handler(constant.CRUD_SDDC, event)
  message_handler(constant.TASK_WH, event)

  event.update(
    {"status": "task_started"}
  )
  call_lambda("check_task", event)
