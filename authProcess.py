#!/usr/bin/env python

from scapy.all import RadioTap, Dot11, Dot11Auth, sendp
import struct
import constants


## Build Auth Response
def dot11_auth_resp(receiver, sender, bssid, sc):
    auth_packet = RadioTap(len=18, present='Flags+Rate+Channel+dBm_AntSignal+Antenna',
                           notdecoded='\x00\x6c' + struct.pack("<h", 2457) + '\xc0\x00\xc0\x01\x00\x00') \
                  / Dot11(subtype=0x0B, addr1=receiver, addr2=sender, addr3=bssid, SC=sc) \
                  / Dot11Auth(algo=0, seqnum=0x02, status='success')

    sendp(auth_packet, iface=constants.DEVICE_NAME, verbose=False)
