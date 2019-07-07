import json
import boto3

from vmcjp.utils.cron import get_next_time

def put_event(minutes, data):
  lambda_arn = "arn:aws:lambda:ap-northeast-1:{}:function:{}".format(
    data["cloudwatch_account"], 
    data["lambda_name"]
  )
  event_arn = "arn:aws:events:ap-northeast-1:{}:rule/{}".format(
    data["cloudwatch_account"], 
    data["event_name"]
  )
  
  boto3.client("events").put_rule(
    Name=data["event_name"],
    ScheduleExpression=get_next_time(minutes)
  )

  boto3.client("events").put_targets(
    Rule=data["event_name"],
    Targets=[
      {
        "Id": data["lambda_name"],
        "Arn": lambda_arn,
        "Input": json.dumps(data)
      }
    ]
  )
  
  boto3.client("lambda").add_permission(
    FunctionName=data["lambda_name"],
    StatementId=data["event_name"],
    Action="lambda:InvokeFunction",
    Principal="events.amazonaws.com",
    SourceArn=event_arn
  )

def remove_event(event_name, lambda_name):
  boto3.client("events").remove_targets(
    Rule=event_name,
    Ids=[
        event_name
    ]
  )
  
  boto3.client("lambda").remove_permission(
    FunctionName=lambda_name,
    StatementId=event_name,
  )  
  
