# If on Windows install Npcap
# Also pip install scapy
from scapy.all import *

ip1 = IP(src = "localhost", dst = "192.168.0.11")
sy1 = TCP(sport = 1024, dport = 137, flags = "A", seq = 12345)

packet = ip1 / sy1

p = sr1(packet)

p.show()

# An output with no response or an ICMP Error means there is a firewall
