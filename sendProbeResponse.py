#!/usr/bin/env python

from scapy.all import *
import constants

## Wifi interface
device = constants.DEVICE_NAME


## Handling the packet
def packet_handler(packet):
    if packet.haslayer(Dot11):  # 802.11
        if packet.type == 0 and packet.subtype == 4:  # Probe request
            if packet.ID == 0:
                if packet.info == constants.SSID:  # Our SSID
                    dot11_probe_resp()




## Build Probe Response
def dot11_probe_resp():
    # TODO - make better fields (https://github.com/dinosec/iStupid/blob/master/iStupid.py)

    # Initial beacon timestamp
    ts = 00000000L

    # Privacy setting on: probe response header
    probresp_header = Dot11ProbeResp(timestamp=ts, beacon_interval=constants.BEACON_INTERVAL, \
                                     cap="short-preamble+short-slot+privacy")

    # Rates header
    rates_header = Dot11Elt(ID="Rates", info='\x82\x84\x8b\x16')

    probe_response_packet = RadioTap()/Dot11(addr1='da:a1:19:cb:4f:5f',addr2=constants.BEACON_ADDR2,addr3=constants.BEACON_ADDR3)/\
        probresp_header/\
        Dot11Elt(ID="SSID",info=constants.SSID)/\
        Dot11Elt(ID="DSset",info='x03')/\
        rates_header/\
        Dot11Elt(ID=221,info="\x50\x6F\x9A\x09"+   # P2P
        	"\x02"+"\02\x00"+"\x21\x00"+       # P2P Capabilities
        	"\x0D"+"\x1B\x00"+
                mac2str(constants.BEACON_ADDR2)+
                "\x01\x88"+
                "\x00\x0A\x00\x50\xF2\x04\x00\x05"+
                "\x00"+
                "\x10\x11"+
                "\x00\x06"+
                "fafa\xFA\xFA")                    # P2P Device Info

    sendp(probe_response_packet, iface=device, verbose=False)


print 'Press CTRL+C to Abort'

## Setup sniff
sniff(iface=device, prn=packet_handler)
