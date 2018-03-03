#!/usr/bin/env python

from scapy.all import *
import constants

## Wifi interface, time
device = constants.DEVICE_NAME
ftime = time.time() * 1000000


## Uptime function
def uptime():
    microtime = int(round(time.time() * 1000000)) - ftime
    return microtime


## Handling the packet
def packet_handler(packet):
    if packet.haslayer(Dot11):  # 802.11
        if packet.type == 0 and packet.subtype == constants.PROBE_REQ:  # Probe request
            if packet.ID == 0:
                if packet.info == '':  # Our SSID / TODO - will be replaced with constants.SSID
                    print('.')
                    dot11_probe_resp(packet.addr2)


## Build Probe Response
def dot11_probe_resp(destaddr):
    # TODO - make better fields (https://github.com/dinosec/iStupid/blob/master/iStupid.py
    # TODO - https://github.com/0x90/wifi-scripts/blob/cde03cb610d7fd4ebd55bd8e45063895d1b06526/AP/fuzzap.py)

    # Privacy setting on: probe response header
    probresp_header = Dot11ProbeResp(timestamp=uptime(), beacon_interval=constants.BEACON_INTERVAL, \
                                     cap="short-preamble+short-slot+privacy")

    # Rates header
    rates_header = Dot11Elt(ID="Rates", info='\x82\x84\x8b\x16')

    probe_response_packet = (RadioTap(present=18479L) /
                             Dot11(addr2=constants.BSSID, addr3=constants.BSSID, addr1=destaddr, FCfield=8L) /
                             probresp_header /
                             Dot11Elt(info=constants.SSID, ID=0) /
                             Dot11Elt(info=rates_header, ID=1) /
                             Dot11Elt(info='\x01', ID=3, len=1) /
                             Dot11Elt(info='\x00', ID=42, len=1) /
                             Dot11Elt(
                                 info='\x01\x00\x00\x0f\xac\x02\x02\x00\x00\x0f\xac\x02\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x02(\x00',
                                 ID=48, len=24) /
                             Dot11Elt(info='H`l', ID=50, len=3))

    sendp(probe_response_packet, iface=device, verbose=False)


print 'Press CTRL+C to Abort'

## Setup sniff
sniff(iface=device, prn=packet_handler)
