#!/usr/bin/env python

from scapy.all import RadioTap, Dot11, Dot11Auth, sendp
import struct


## Build Auth Response
def dot11_auth_resp(receiver, sender, bssid, sc, device):
    auth_packet = RadioTap() \
                  / Dot11(subtype=0x0B, addr1=receiver, addr2=sender, addr3=bssid, SC=sc) \
                  / Dot11Auth(algo=0, seqnum=0x02, status='success')

    sendp(auth_packet, iface=device, verbose=False)
