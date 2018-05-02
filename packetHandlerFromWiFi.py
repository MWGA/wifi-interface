from scapy.all import *

import constants
import probeProcess
import restClient
import swapHeaders


## Handling the packet
def packet_handler(packet):
    if packet.haslayer(Dot11):  # 802.11
        if packet.type == 0 and packet.subtype == constants.PROBE_REQ:  # Probe request
            if packet.ID == 0:
                if packet.info == '':
                    probeProcess.dot11_probe_resp(packet.addr2)
                elif packet.info == constants.SSID:
                    print('probe')
                    restClient.generate_lvap(packet.addr2, "WTP1")
                    # TODO - send probe response with new BSSID
        if packet.type == 0 and packet.subtype == constants.AUTH_REQ:  # Auth request
            print ('authentication')
            # TODO - handle authentication
        if packet.type == 0 and packet.subtype == constants.ASSOC_REQ:  # Assoc request
            print ('association')
            # TODO - handle association
        if packet.type == 2:
            print ('data')
            swapHeaders.removeWiFiHeaderAndAddEthernet(packet)


def start():
    ## Setup sniff
    sniff(iface=constants.DEVICE_NAME, prn=packet_handler)
