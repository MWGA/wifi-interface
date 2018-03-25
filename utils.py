from scapy.all import *

import constants


## Add to Ethernet layer as payload
def addToEth(packet):
    data = packet
    ether = Ether(src=constants.MAC_SRC, dst=constants.MAC_DST, type=0x804)
    payload = Raw(load=data)
    packetout = ether / payload
    return packetout
