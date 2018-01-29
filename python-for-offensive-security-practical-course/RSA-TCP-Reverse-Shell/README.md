

RSA TCP Reverse shell:

0. generate on both hosts pair of keys

1. copies public keys between hosts

2. on Win use: RSA - Client - TCP Reverse Shell.py, put kali public key and your own private key

3. on Kali use: RSA - Server- TCP Reverse Shell.py  plus put win public key and then put your private key



#############################
Generate random AES which will use for RSA transmission:


Win : Hybrid - Client - TCP Reverse Shell.py with own private key

Kali: Hybrid - Server- TCP Reverse Shell.py with Win public key
Ten random AES will be generated on Kali site