from scapy.all import Dot11, Dot11Beacon, Dot11Elt, RadioTap, sendp, hexdump

import constants
import struct


def transmitBeacons():
    ## Define fields
    netSSID = constants.SSID  # SSID
    device = constants.DEVICE_NAME  # Interface name here

    dot11 = Dot11(type=0, subtype=8, addr1=constants.BEACON_ADDR1,
                  addr2=constants.DEVICE_MAC, addr3=constants.DEVICE_MAC)
    beacon = Dot11Beacon(cap='ESS')
    frame = RadioTap() / \
            dot11 / \
            beacon / \
            Dot11Elt(ID="SSID", len=len(netSSID), info=netSSID) / \
            Dot11Elt(ID="Rates", info=constants.RATES) / \
            Dot11Elt(ID="DSset", info="\x03") / \
            Dot11Elt(ID="TIM", info="\x00\x01\x00\x00")

    frame.show()

    ## Print Hex frame
    print("\nHexdump of frame:")
    hexdump(frame)

    ## Generate frames with interval 0.1 second
    sendp(frame, iface=device, inter=constants.BEACON_INTERVAL, loop=1, verbose=False)
