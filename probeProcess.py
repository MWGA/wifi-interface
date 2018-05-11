#!/usr/bin/env python

from scapy.all import *

import constants

## Wifi interface, time
ftime = time.time() * 1000000


## Uptime function
def uptime():
    microtime = int(round(time.time() * 1000000)) - ftime
    return microtime


## Build Probe Response
def dot11_probe_resp(destaddr, device):
    # TODO - make better fields (https://github.com/dinosec/iStupid/blob/master/iStupid.py
    # TODO - https://github.com/0x90/wifi-scripts/blob/cde03cb610d7fd4ebd55bd8e45063895d1b06526/AP/fuzzap.py)

    # Privacy setting on: probe response header
    probresp_header = Dot11ProbeResp(timestamp=uptime(), beacon_interval=constants.BEACON_INTERVAL, \
                                     cap="short-preamble+short-slot+privacy")

    # Rates header
    rates_header = Dot11Elt(ID="Rates", info=constants.RATES)

    probe_response_packet = (RadioTap(present=18479L) /
                             Dot11(addr2=constants.BSSID, addr3=constants.BSSID, addr1=destaddr, FCfield=8L) /
                             probresp_header /
                             Dot11Elt(info=constants.SSID, ID=0) /
                             Dot11Elt(info=rates_header, ID=1) /
                             Dot11Elt(info='\x01', ID=3, len=1) /
                             Dot11Elt(info='\x00', ID=42, len=1) /
                             Dot11Elt(
                                 info=constants.RSN,
                                 ID=48, len=24) /
                             Dot11Elt(info='H`l', ID=50, len=3))

    sendp(probe_response_packet, iface=device, verbose=False)