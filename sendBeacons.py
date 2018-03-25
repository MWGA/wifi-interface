from scapy.all import Dot11, Dot11Beacon, Dot11Elt, RadioTap, sendp, hexdump

import constants

# TODO - make open WiFi
## Define fields
netSSID = constants.SSID  # SSID
device = constants.DEVICE_NAME  # Interface name here

dot11 = Dot11(type=0, subtype=8, addr1=constants.BEACON_ADDR1,
              addr2=constants.BEACON_ADDR2, addr3=constants.BEACON_ADDR3)
beacon = Dot11Beacon(cap="short-preamble+short-slot+ESS")
essid = Dot11Elt(ID='SSID', info=netSSID, len=len(netSSID))
rsn = Dot11Elt(ID='RSNinfo', info=constants.RSN)  # RSN Capabilities (no extra capabilities)

## Build the frame
frame = RadioTap() / dot11 / beacon / essid / rsn
frame.show()

## Print Hex frame
print("\nHexdump of frame:")
hexdump(frame)
raw_input("\nPress enter to start\n")

print 'Press CTRL+C to Abort'

## Generate frames with interval 0.1 second
sendp(frame, iface=device, inter=constants.BEACON_INTERVAL, loop=1)
