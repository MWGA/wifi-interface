#!/usr/bin/env python

from scapy.all import *

import constants
import utils

## Counter and wifi interface
counter = 0
device = constants.DEVICE_NAME


## Handling the packet
def removeWiFiHeaderAndAddEthernet(packet):
    global counter
    counter += 1
    packetout = ''
    # TODO - remove WiFi header
    # Add Ethernet padding
    if packet.haslayer(Dot11):  # 802.11
        if packet.type == 2:
            packetout = utils.addToEth(packet)
            # Dump into pcap file
            wrpcap('monitor_capture.pcap', packetout, append=True)

    # Send packet via virtual interface
    sendp(packetout, iface=constants.TO_OVS_DEVICE, verbose=False)

