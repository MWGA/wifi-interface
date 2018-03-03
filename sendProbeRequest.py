#!/usr/bin/env python

from scapy.all import sendp,Dot11,RadioTap,RandMAC
import constants


# Injection device
device = constants.DEVICE_NAME

# Time betwen frames send. Set 0 to unlimited
interval = 0.5

print 'Press CTRL+C to Abort'

# Send Probe Request
sendp(RadioTap() /
      Dot11(type=0, subtype=4,
            addr1=constants.BROADCAST_ADDR,
            addr2=RandMAC(),
            addr3=constants.BROADCAST_ADDR),
      iface=device, loop=1, inter=interval)
