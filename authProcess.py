#!/usr/bin/env python

from scapy.all import *
import constants

## Wifi interface
device = constants.DEVICE_NAME


## Handling the packet
def packet_handler(packet):
    if packet.haslayer(Dot11):  # 802.11
        if packet.type == 0 and packet.subtype == constants.AUTH_REQ:  # Auth request
            print('auth')
            packet.show()


## Build Auth Response
def dot11_auth_resp():
    # TODO - diiscuss this
    auth_response_packet = ''

    sendp(auth_response_packet, iface=device, verbose=False)


print 'Press CTRL+C to Abort'

## Setup sniff
sniff(iface=device, prn=packet_handler)
