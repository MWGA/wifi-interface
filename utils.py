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


def next_sc(sc):
    sc = (sc + 1) % 4096
    temp = sc
    return temp * 16  # Fragment number -> right 4 bits


def next_aid(aid):
    aid = (aid + 1) % 2008
    return aid
