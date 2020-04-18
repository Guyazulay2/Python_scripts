#######

Paramiko form python to aws ec2

#######

import paramiko

user_name="ubuntu"
passwd="rootroot"
ip="18.223.44.129"
print("Please wait, creating ssh client ####")
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("Please wait, connecting with remoter server ####")
ssh_client.connect(hostname=ip,username=user_name,password=passwd)

cmd="ls -lrt /home/ubuntu"
stdin,stdout,stderr=ssh_client.exec_command(cmd)
stdout=stdout.readlines()
print(stdout)
