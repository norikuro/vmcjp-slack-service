import json
import boto3
    
def write_json_to_s3(bucket, key, dictionary):
    s3 = boto3.resource('s3')
    s3obj = s3.Object(bucket, key)
    s3obj.put(Body=json.dumps(dictionary, indent=2))
    
def read_json_from_s3(bucket, key):
    s3 = boto3.resource('s3')
    return json.loads(s3.Object(bucket, key).get()['Body'].read())

def download_from_s3(bucket, key, target):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    bucket.download_file(key, target)
