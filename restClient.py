import requests

import constants
from LVAP import LVAP

url = 'http://10.62.45.184:4567/lvap'


def generate_lvap(mac, wtp):
    response = requests.post(url, json={
        "mac": str(mac),
        "ssid": str(constants.SSID),
        "wtp": str(wtp)
    })

    constants.LVAP_CONTEXT.append(LVAP('10.10.10.1', str(mac), response.json()['bssid'], str(constants.SSID), str(wtp)))

    print(response.json())

# generate_lvap("ff:ff:ff:ff:ff:ff",str(constants.DEVICE_NAME))
