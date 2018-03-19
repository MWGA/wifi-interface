import re
import socket

import constants


## IP address validation
def IPvalid(IP):
    try:
        socket.inet_aton(IP)
        return IP
    except socket.error:
        return 'Error: IP address not valid'


## MAC address validation
def MACvalid(MAC):
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", MAC.lower()):
        return MAC
    else:
        return 'Error: MAC address not valid'


## class LVAP
class LVAP(object):
    """Light virtual Access Point class"""
    SSID = constants.SSID

    def __init__(self, IPaddress, MACaddress, BSSID, WTP):
        self.IPaddress = IPvalid(IPaddress)
        self.MACaddress = MACvalid(MACaddress)
        self.BSSID = MACvalid(BSSID)
        self.WTP = WTP

    def show(self):
        print('IP address -> {} \nMAC address -> {} \nBSSID -> {} \nSSID -> {} \nWTP -> {}'.format(self.IPaddress,
                                                                                                   self.MACaddress,
                                                                                                   self.BSSID,
                                                                                                   self.SSID, self.WTP))


# Testing
lv = LVAP('10.10.10.10', 'ff:ff:ff:ff:ff:ff', '02:02:02:02:02:02', constants.DEVICE_NAME)

lv.show()
