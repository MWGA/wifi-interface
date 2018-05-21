#!/usr/bin/env python

from scapy.all import *

import constants
import struct

## Wifi interface, time
ftime = time.time() * 1000000


## Uptime function
def uptime():
    microtime = int(round(time.time() * 1000000)) - ftime
    return microtime


## Build Probe Response
def dot11_probe_resp(bssid, destaddr, wtpmac, device, sc):

    probe_response_packet = RadioTap(len=18, present='Flags+Rate+Channel+dBm_AntSignal+Antenna',
                                     notdecoded='\x00\x6c' + struct.pack("<h", 2412) + '\xc0\x00\xc0\x01\x00\x00') \
                            / Dot11(subtype=5, addr1=destaddr, addr2=wtpmac, addr3=bssid, SC=sc) \
                            / Dot11ProbeResp(timestamp=time.time(), beacon_interval=constants.BEACON_INTERVAL,
                                             cap='ESS') \
                            / Dot11Elt(ID='SSID', info=constants.SSID) \
                            / Dot11Elt(ID='Rates', info=constants.RATES)

    sendp(probe_response_packet, iface=device, verbose=False)