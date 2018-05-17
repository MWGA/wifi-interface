#!/usr/bin/env python

from scapy.all import RadioTap, Dot11, Dot11Auth, sendp
import utils


## Build Auth Response
def dot11_auth_resp(receiver, sender, bssid, sc, device):
    auth_packet = RadioTap(present=18479L) \
                  / Dot11(subtype=0x0B, addr1=receiver, addr2=sender, addr3=bssid, SC=sc)

    sendp(auth_packet, iface=device, verbose=False)
