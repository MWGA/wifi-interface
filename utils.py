from scapy.all import RadioTap, Ether, Raw

import constants


## Add to Ethernet layer as payload
def addToEth(packet):
    data = packet
    ether = Ether(src=constants.MAC_SRC, dst=constants.MAC_DST, type=0x804)
    payload = Raw(load=data)
    packetout = ether / payload
    return packetout


## Remove Ethernet layer and add Radiotap
def removeEth(packet):
    dot11payload = packet.getlayer(Raw)
    packetout = RadioTap() / dot11payload
    return packetout
