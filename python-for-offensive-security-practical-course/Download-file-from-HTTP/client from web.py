import socket                   # Import socket module

s = socket.socket()             # Create a socket object#
#host = socket.gethostname()     # Get local machine name
#port = 60000                    # Reserve a port for your service.

#s.connect(('10.10.10.100', port))
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.10.10.100', 8081))
s.send("Hello server!")

with open('C:\j\j.txt', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
