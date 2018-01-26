#from scapy.all import *
import sys
from scapy.all import sr1,IP,ICMP
ip1 = scapy.IP(src="10.10.10.10", dst ="10.10.10.100" )
tcp1 = TCP(sport =1024, dport=80, flags="S", seq=12345)
packet = ip1/tcp1
p =sr1(packet, inter=1)
p.show()
rs1 = TCP(sport =1024, dport=80, flags="R", seq=12347)
packet1=ip1/rs1
p1 = sr1(packet1)
p1.show
