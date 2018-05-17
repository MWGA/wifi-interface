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
def dot11_probe_resp(bssid, destaddr, wtpmac, device, sc):
    # Privacy setting on: probe response header
    probresp_header = Dot11ProbeResp(timestamp=uptime(), beacon_interval=constants.BEACON_INTERVAL, \
                                     cap='ESS')

    # Rates header
    rates_header = Dot11Elt(ID="Rates", info=constants.RATES)

    #    probe_response_packet = (RadioTap(present=18479L) /
    #                             Dot11(addr2=wtpmac, addr3=bssid, addr1=destaddr, FCfield=8L) /
    #                             probresp_header /
    #                             Dot11Elt(info=constants.SSID, ID=0) /
    #                             Dot11Elt(info=rates_header, ID=1) /
    #                             Dot11Elt(info='\x01', ID=3, len=1) /
    #                             Dot11Elt(info='\x00', ID=42, len=1) /
    #                             Dot11Elt(info='H`l', ID=50, len=3))

    probe_response_packet = RadioTap(len=18, present='Flags+Rate+Channel+dBm_AntSignal+Antenna',
                                     notdecoded='\x00\x6c' + struct.pack("<h", 2484) + '\xc0\x00\xc0\x01\x00\x00') \
                            / Dot11(subtype=5, addr1=destaddr, addr2=wtpmac, addr3=bssid, SC=sc) \
                            / Dot11ProbeResp(timestamp=ftime, beacon_interval=0x0064, cap=0x2104) \
                            / Dot11Elt(ID='SSID', info=constants.SSID) \
                            / Dot11Elt(ID='Rates', info=constants.RATES)

    sendp(probe_response_packet, iface=device, verbose=False)