Kali: Data exfiltration Server - TCP reverse shell.py


Win Target: Low level port scanner.py

formula:

scan IP:Port/s

for instance : scan 10.10.10.100:20,21,80


TCP scanner, to support UDP, modify like below:

The second argument determines the socket type; socket.SOCK_DGRAM is UDP, socket.SOCK_STREAM is a TCP socket. This all provided you are using a AF_INET or AF_INET6socket family.

