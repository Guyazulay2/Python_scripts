import boto3
import uuid
from urllib.parse import unquote_plus
import xml.etree.ElementTree as ET
import json
import paramiko
import time


region = 'us-west-1'
instances = ['i-035d75d3d4ec952c6']
ec2 = boto3.client('ec2', region_name= region)

def lambda_handler(event, context):
    print(f"Received raw event: {event}")
    
    # Bucket Name where file was uploaded
    source_bucket_name = event['Records'][0]['s3']['bucket']['name']

    # Filename of object (with path)
    file_key_name = event['Records'][0]['s3']['object']['key']
    ec2.start_instances(InstanceIds=instances)
    
    print('-------------------')
    print('started the instance: ' + str(instances))
    time.sleep(60)
    
    s3_client = boto3.client('s3')
    s3_client.download_file('sshay', 'guy.pem', '/tmp/guykey.pem')
    time.sleep(20)
    
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privkey = paramiko.RSAKey.from_private_key_file('/tmp/guykey.pem')
    ssh.connect(hostname='52.8.233.224', username='ubuntu', pkey=privkey)
    
    print("Connected to :" + hostname)
    
    commands = [
        "docker run -d -v /home/ubuntu/new/vals:/root/apps/vals data_processing python /root/apps/basic.py"
        ""
        ]

    # executing list of commands within server
    for command in commands:
        print("Executing {command}")
        stdin , stdout, stderr = ssh_.exec_command(command)
        print(stdout.read())
        print(stderr.read())
