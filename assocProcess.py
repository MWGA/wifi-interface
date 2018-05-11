#!/usr/bin/env python

from scapy.all import *

import constants

ftime = time.time() * 1000000


## Uptime function
def uptime():
    microtime = int(round(time.time() * 1000000)) - ftime
    return microtime


## Build Auth Response
def dot11_assoc_resp(device, receiver, sender, bssid):
    # TODO - make better fields
    probresp_header = Dot11ProbeResp(timestamp=uptime(), beacon_interval=constants.BEACON_INTERVAL, \
                                     cap="short-preamble+short-slot+privacy")

    rates_header = Dot11Elt(ID="Rates", info=constants.RATES)

    assoc_response_packet = (RadioTap(present=18479L) /
                             Dot11(subtype=0x01, addr2=sender, addr3=bssid, addr1=receiver,
                                   FCfield=8L) /
                             probresp_header /
                             Dot11AssoResp(cap=0x2104, status=0, AID='') /  # self.ap.next_aid()) /
                             rates_header)

    sendp(assoc_response_packet, iface=device, verbose=False)

