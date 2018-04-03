#!/usr/bin/env python

from scapy.all import *

import constants
import utils

## Counter and wifi interface
counter = 0
device = constants.DEVICE_NAME


def send_encapsulate(packet):
    packetout = utils.removeEth(packet)

    packetout.show()
    # Send packet via wireless interface
    sendp(packetout, iface=constants.DEVICE_NAME, verbose=False)  # TODO - malformed and oversized packets


print 'Press CTRL+C to Abort'

## Setup sniff
sniff(offline='monitor_capture.pcap', prn=send_encapsulate)  # TODO - reroute from veth1 interface
