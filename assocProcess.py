#!/usr/bin/env python

from scapy.all import *

import constants

## Wifi interface
device = constants.DEVICE_NAME
ftime = time.time() * 1000000


## Uptime function
def uptime():
    microtime = int(round(time.time() * 1000000)) - ftime
    return microtime


## Handling the packet
def packet_handler(packet):
    if packet.haslayer(Dot11):  # 802.11
        if packet.type == 0 and packet.subtype == constants.ASSOC_REQ:  # Assoc request
            print('assoc')
            packet.show()
            # dot11_assoc_resp(packet.addr2)


## Build Auth Response
def dot11_assoc_resp(destaddr):
    # TODO - make better fields
    probresp_header = Dot11ProbeResp(timestamp=uptime(), beacon_interval=constants.BEACON_INTERVAL, \
                                     cap="short-preamble+short-slot+privacy")

    rates_header = Dot11Elt(ID="Rates", info='\x82\x84\x8b\x16')

    assoc_response_packet = (RadioTap(present=18479L) /
                             Dot11(subtype=0x01, addr2=constants.BSSID, addr3=constants.BSSID, addr1=destaddr,
                                   FCfield=8L) /
                             probresp_header /
                             Dot11AssoResp(cap=0x2104, status=0, AID='') /  # self.ap.next_aid()) /
                             rates_header)

    sendp(assoc_response_packet, iface=device, verbose=False)


print 'Press CTRL+C to Abort'

## Setup sniff
sniff(iface=device, prn=packet_handler)
