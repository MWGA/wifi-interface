#!/usr/bin/env python

from scapy.all import *

## Counter and wifi interface
counter = 0
interface = "wlx98ded0054dc9"


## Handling the packet
def receive_encapsulate(packet):
    global counter
    counter += 1
    # Dump into pcap file
    wrpcap('filtered.pcap', packet, append=True)
    pad_len = 60 - len(packet)
    pad = Padding()
    pad.load = '\x00' * pad_len
    packet = packet / pad
    # Send packet via virtual interface
    sendp(packet, iface="veth0")


## Setup sniff
sniff(iface=interface, prn=receive_encapsulate)