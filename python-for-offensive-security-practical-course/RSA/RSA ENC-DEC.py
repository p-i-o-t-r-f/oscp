# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

# Download Pycrypto for Windows - pycrypto 2.6 for win32 py 2.7
# http://www.voidspace.org.uk/python/modules.shtml#pycrypto

# Download Pycrypto source
# https://pypi.python.org/pypi/pycrypto
# For Kali, after extract the tar file, invoke "python setup.py install"from Crypto.PublicKey import RSA

from Crypto.PublicKey import RSA

def encrypt(message):
    publickey = open("public.pem", "r")
    encryptor = RSA.importKey(publickey)
    global encriptedData
    '''
The encrypt function, will take two arguments, the second one can be discarded
>>that's why we passed (message,0) arguments

The retunred value is a tuple with two items. The first item is the
ciphertext. The second item is always None.
>>that's why print encriptedData[0]

Ref: https://pythonhosted.org/pycrypto/Crypto.PublicKey.RSA._RSAobj-class.html#encrypt
    '''
    encriptedData=encryptor.encrypt(message,0)
    print encriptedData[0]

encrypt('Hussam')


def decrypt(cipher):
    privatekey = open("private.pem", "r")
    decryptor = RSA.importKey(privatekey)
    print decryptor.decrypt(cipher)    

decrypt(encriptedData)



