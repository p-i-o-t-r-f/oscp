import os
ip = raw_input("ENter the ip ")
#net = raw_input("Enter the Network Address ")
#net1= net.split('.')
#print net1
#a = '.'
#net2 = net1[0]+a+net1[1]+a+net1[2]+a + net1[3]
response = os.popen(("ping -n 1 " +  ip ))
for line in response.readlines():
 print line,
