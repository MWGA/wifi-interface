#!/usr/bin/env python

from scapy.all import *
import constants

## Counter and wifi interface
counter = 0
device = constants.DEVICE_NAME


## Handling the packet
def receive_encapsulate(packet):
    global counter
    counter += 1
    # Dump into pcap file
    wrpcap('monitor_capture.pcap', packet, append=False)

    # Add Ethernet padding - TODO make better padding for this solution
    if packet.haslayer(Dot11):  # 802.11
        pad_len = 60 - len(packet)
        pad = Padding()
        pad.load = '\x00' * pad_len
        packet = packet / pad

    # Send packet via virtual interface
    sendp(packet, iface="veth0")


print 'Press CTRL+C to Abort'

## Setup sniff
sniff(iface=device, prn=receive_encapsulate)
