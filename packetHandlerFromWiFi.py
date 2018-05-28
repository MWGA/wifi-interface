from scapy.all import *

import assocProcess
import authProcess
import constants
import probeProcess
import restClient
import swapHeaders
import LVAP
import utils
import state

## Handling the packet
def start():
    ## Setup sniff
    sniff(iface=constants.DEVICE_NAME, prn=packet_handler)


def packet_handler(packet):
    if packet.haslayer(Dot11) and packet.addr2 == constants.DEVICE_MAC or packet.addr1 == constants.BROADCAST_ADDR: #packet.haslayer(Dot11):  # 802.11
        s = state.State()

        if packet.FCfield.retry:
            s.dropped = s.dropped + 1
            return

        if packet.haslayer(Dot11ProbeReq):

            if packet.addr1 == constants.BROADCAST_ADDR:  # Active scanning
                print "as " + str(s.active_scans) + " from " + packet.addr2
                s.active_scans = s.active_scans + 1
                probeProcess.dot11_probe_resp(packet.addr2, constants.DEVICE_MAC, utils.next_sc(0))
            elif packet.info == constants.SSID:
                print('probe ' + packet.addr2)
                # TODO - change BSSID addr in process
                # tmpBSSID = LVAP.get_bssid(packet.addr2)
                # if not tmpBSSID:
                # restClient.generate_lvap(packet.addr2, constants.DEVICE_NAME)
                # tmpBSSID = LVAP.get_bssid(packet.addr2)
                probeProcess.dot11_probe_resp(constants.DEVICE_MAC, packet.addr2, constants.DEVICE_MAC,
                                              constants.DEVICE_NAME,
                                              utils.next_sc(0))
        if packet.type == 0 and packet.subtype == constants.AUTH_REQ:  # and packet.addr1 == constants.DEVICE_MAC:  # Auth request
            if packet.addr1 == constants.DEVICE_MAC:
                print ('authentication')
                authProcess.dot11_auth_resp(packet.addr2, packet.addr1, packet.addr1, utils.next_sc(0),
                                        constants.DEVICE_NAME)
        if packet.type == 0 and packet.subtype == constants.ASSOC_REQ:  # Assoc request
            if packet.addr1 == constants.DEVICE_MAC:
                print ('association')
                assocProcess.dot11_assoc_resp(constants.DEVICE_NAME, packet.addr2, packet.addr1, packet.addr1)
        if packet.type == 2:
            pass
        if packet.addr1 == constants.DEVICE_MAC:
            print ('data')
            # swapHeaders.removeWiFiHeaderAndAddEthernet(packet)
