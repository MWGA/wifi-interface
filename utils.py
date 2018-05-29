from scapy.all import *

import constants

## Add to Ethernet layer as payload
def addToEth(packet):
    try:
        data = packet.getlayer(SNAP).payload.original
        ether = Ether(src=packet.addr1, dst=packet.addr2, type=payload_name_to_ethtype(packet.getlayer(SNAP).payload.name))
        packetout = ether / data
        return packetout
    except:
        return False



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

def payload_name_to_ethtype(name):
    if name == "ARP":
        return 0x0806
    raise Exception
