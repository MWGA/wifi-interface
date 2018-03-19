#!/usr/bin/env python

from scapy.all import *

import constants
import utils

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
        if packet.type == 2:
            packetout = utils.addToEth(packet)

    # Send packet via virtual interface
    sendp(packetout, iface=constants.TO_OVS_DEVICE, verbose=False)


print 'Press CTRL+C to Abort'

## Setup sniff
sniff(iface=device, prn=receive_encapsulate)
