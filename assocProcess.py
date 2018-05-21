#!/usr/bin/env python
from scapy.layers.dot11 import Dot11Elt, Dot11AssoResp, Dot11, RadioTap, Dot11ProbeResp

from scapy.all import *
import utils
import constants

ftime = time.time() * 1000000


## Uptime function
def uptime():
    microtime = int(round(time.time() * 1000000)) - ftime
    return microtime


## Build Auth Response
def dot11_assoc_resp(receiver, sender, bssid):
    probresp_header = Dot11ProbeResp(timestamp=uptime(), beacon_interval=constants.BEACON_INTERVAL, cap='ESS')

    rates_header = Dot11Elt(ID="Rates", info=constants.RATES)

    assoc_response_packet = RadioTap(len=18, present='Flags+Rate+Channel+dBm_AntSignal+Antenna',
                                     notdecoded='\x00\x6c' + struct.pack("<h", 2412) + '\xc0\x00\xc0\x01\x00\x00') \
                            / Dot11(subtype=0x01, addr2=sender, addr3=bssid, addr1=receiver) \
                            / Dot11AssoResp(status=0, AID=utils.next_aid(10)) \
                            / rates_header

    sendp(assoc_response_packet, iface=constants.DEVICE_NAME, verbose=False, count=1)

