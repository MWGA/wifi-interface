## Add to UDP
def addToUDP(packet):
    data = packet
    ether = Ether(src=constants.MAC_SRC, dst=constants.MAC_DST)
    ip = IP(src=constants.IP_SRC, dst=constants.IP_DST)
    udp = UDP(sport=constants.SRC_PORT, dport=constants.DST_PORT)
    payload = Raw(load=data)
    packetout = ether / ip / udp / payload
    return packetout


## Add to Ethernet II
def addToEth(packet):
    pad_len = 60 - len(packet)
    pad = Padding()
    pad.load = '\x00' * pad_len
    packetout = packet / pad
    return packetout
