from scapy.all import *

import assocProcess
import authProcess
import constants
import probeProcess
import restClient
import swapHeaders
import LVAP
import utils


## Handling the packet
def start():
    ## Setup sniff
    sniff(iface=constants.DEVICE_NAME, prn=packet_handler)


def packet_handler(packet):
    if packet.haslayer(Dot11):  # 802.11
        if packet.type == 0 and packet.subtype == constants.PROBE_REQ:  # Probe request
            if packet.info == '' and packet.addr1 == 'ff:ff:ff:ff:ff:ff':
                print('as ' + packet.addr2)
                probeProcess.dot11_probe_resp(constants.DEVICE_MAC, packet.addr2, constants.DEVICE_MAC,
                                              constants.DEVICE_NAME, utils.next_sc(0))
            elif packet.info == constants.SSID:
                if packet.addr1 == constants.DEVICE_MAC:
                    print('probe ' + packet.addr2)
                    # TODO - change BSSID addr in process
                    tmpBSSID = LVAP.get_bssid(packet.addr2)
                    if not tmpBSSID:
                        restClient.generate_lvap(packet.addr2, constants.DEVICE_NAME)
                        tmpBSSID = LVAP.get_bssid(packet.addr2)
                    probeProcess.dot11_probe_resp(tmpBSSID, packet.addr2, constants.DEVICE_MAC,
                                                  constants.DEVICE_NAME,
                                                  utils.next_sc(0))
        if packet.type == 0 and packet.subtype == constants.AUTH_REQ:  # Auth request
            if packet.addr1 == constants.DEVICE_MAC:
                print ('authentication')
                tmpBSSID = LVAP.get_bssid(packet.addr2)
                if not tmpBSSID:
                    print('invalid auth')
                authProcess.dot11_auth_resp(packet.addr2, packet.addr1, tmpBSSID, utils.next_sc(0),
                                            constants.DEVICE_NAME)
        if packet.type == 0 and packet.subtype == constants.ASSOC_REQ:  # Assoc request
            if packet.addr1 == constants.DEVICE_MAC:
                print ('association')
                tmpBSSID = LVAP.get_bssid(packet.addr2)
                if not tmpBSSID:
                    print('invalid assoc')
                assocProcess.dot11_assoc_resp(constants.DEVICE_NAME, packet.addr2, packet.addr1, tmpBSSID)

        if packet.type == 2 and packet.subtype == 0:
            print ('data')
            p = utils.addToEth(packet)
            # if p is not False:
            # x    sendp(p, iface=constants.TO_OVS_DEVICE, verbose=False)

        if packet.addr1 == constants.DEVICE_MAC:
            pass  # swapHeaders.removeWiFiHeaderAndAddEthernet(packet)
