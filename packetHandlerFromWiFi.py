from scapy.all import *

import assocProcess
import authProcess
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
                    probeProcess.dot11_probe_resp(packet.addr2, constants.DEVICE_NAME)
                elif packet.info == constants.SSID and packet.addr1 == constants.DEVICE_MAC:
                    print('probe')
                    jsonBSSID = restClient.generate_lvap(packet.addr2, constants.DEVICE_NAME)
                    # BSSID = jsonBSSID.json('mac')
                    # TODO - send probe response with new BSSID
        if packet.type == 0 and packet.subtype == constants.AUTH_REQ:  # Auth request
            if packet.addr1 == constants.DEVICE_MAC:
                print ('authentication')
                authProcess.dot11_auth_resp(packet.addr2, packet.addr1, constants.BSSID, 0, constants.DEVICE_NAME)
                # TODO - change BSSID
        if packet.type == 0 and packet.subtype == constants.ASSOC_REQ:  # Assoc request
            if packet.addr1 == constants.DEVICE_MAC:
                print ('association')
                assocProcess.dot11_assoc_resp(constants.DEVICE_NAME, packet.addr1, packet.addr2, constants.BSSID)
                # TODO - change BSSID
        if packet.type == 2:
            if packet.addr1 == constants.DEVICE_MAC:
                print ('data')
                swapHeaders.removeWiFiHeaderAndAddEthernet(packet)


def start():
    ## Setup sniff
    sniff(iface=constants.DEVICE_NAME, prn=packet_handler)

