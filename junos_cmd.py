#!/usr/bin/python

import paramiko,sys
import socket


#Authentication credentials
username='root'
password='juniper123'

#Check command line options
try:
  opt1=sys.argv[1]
  #value1: ip address or file path
  value1=sys.argv[2]
  opt2=sys.argv[3]
  #value2: command
  value2=sys.argv[4]
except IndexError:
  print """Usage:
junos_cmd.py {--ip|--file} {IP_ADDR|FILE_PATH} {--cmd 'COMMAND'}

example: 
junos_cmd.py --ip 192.168.1.1 --cmd 'cli -c "show version\n"'
junos_cmd.py --file /tmp/ip_file.txt 'cli -c "show interfaces"'
       """
  sys.exit()

#Check TCP 22 connection 
def Check_SSH(IP):
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.settimeout(3)
  try:
    s.connect((IP,22))
    s.shutdown(2)
    return True
  except:
    print "%s SSH connection failed" % (IP)
    return False


#Paramiko connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())


def run_cmd(device_ip,cmd,username,password):
  if Check_SSH(device_ip):
    try:
      print "Command: %s is running on %s" % (cmd,device_ip)
      ssh.connect(device_ip,username=username,password=password)
      stdin,stdout,stderr = ssh.exec_command(cmd)
      if len(stderr.readlines()) > 0:
        print stderr.readlines()
      #If verbose print is required
      print stdout.readlines()
    except paramiko.AuthenticationException:
      print "%s Authentication failed" % (device_ip)

def run_batch_cmd(filepath,cmd):
    fd = open (filepath,'r')
    for ip_addr in fd.readlines():
      ip_addr=ip_addr.rstrip()
      run_cmd(ip_addr,cmd,username,password)   

if opt1=="--ip":
   run_cmd(value1,value2,username,password) 
elif opt1=="--file":
   run_batch_cmd(value1,value2)   
