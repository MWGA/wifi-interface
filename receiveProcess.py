#!/usr/bin/env python

from scapy.all import send, IP, ICMP
from scapy.all import *

## Create a Packet Counter
counter = 0
interface = "wlx98ded0054dc9"


## Define our Custom Action function
def receive_encapsulate(packet):
    global counter
    counter += 1
    wrpcap('filtered.pcap', packet, append=True)
    print counter
    send(packet, iface="eth0")


## Setup sniff, filtering for IP traffic
sniff(iface=interface, prn=receive_encapsulate)