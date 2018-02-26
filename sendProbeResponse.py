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
    # TODO - make working probe response
    probe_response_packet = RadioTap(len=18, present='Flags+Rate+Channel+dBm_AntSignal+Antenna',
                                     notdecoded='\x00\x6c' + struct.pack("<h", 2407) + '\xc0\x00\xc0\x01\x00\x00') \
                            / Dot11(subtype=5, addr1=constants.BEACON_ADDR1, addr2=constants.BEACON_ADDR2,
                                    addr3=constants.BEACON_ADDR3,
                                    SC=1000) \
                            / Dot11ProbeResp(timestamp=(time() * 1000000),
                                             beacon_interval=0x0064, cap=0x2104) \
                            / Dot11Elt(ID='SSID', info=constants.SSID) \
                            / Dot11Elt(ID='Rates', info=constants.RATES) \
                            / Dot11Elt(ID='DSset', info=chr(1))

    sendp(probe_response_packet, iface=device, verbose=False)


print 'Press CTRL+C to Abort'

## Setup sniff
sniff(iface=device, prn=packet_handler)
