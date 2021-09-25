"""

Python S3 Get Contents
In the Python file, write a program to access the contents of the bucket coderbytechallengesandbox. In there there might be multiple files, but your program should find the file with the prefix __cb__, and then output the contents of that file. You should use the boto3 module to solve this challenge.

You do not need any access keys to access the bucket because it is public. This post might help you with how to access the bucket.

Example Output
contents of some file
Browse Resources
Search for any help or documentation you might need for this problem. For example: array indexing, Ruby hash tables, etc.


"""

import codecs
import requests
import boto3

from botocore.handlers import disable_signing

line_stream = codecs.getreader("utf-8")

def reformat(body=None):
  if body is not None:
    for line in line_stream(body):
      return line

  else:
    return None

# s3 = boto3.client('s3')
s3 = boto3.resource('s3')
s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
bucket = s3.Bucket('coderbytechallengesandbox')

prefix = "__cb__"
data = [obj for obj in list(bucket.objects.filter(Prefix=prefix)) if obj.key != prefix]
for obj in data:
  key = obj.key
  body = obj.get()['Body']
  print(reformat(body))
