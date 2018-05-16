import requests

import constants
import LVAP

url = 'http://10.62.45.184:4567/lvap'


def generate_lvap(mac, wtp):
    response = requests.post(url, json={
        "mac": mac,
        "ssid": constants.SSID,
        "wtp": wtp
    })

    # constants.LVAP_CONTEXT.append(LVAP("", mac, response.json()['bssid'], str(constants.SSID),str(constants.DEVICE_NAME)))

    print(response.json())

generate_lvap("ff:ff:ff:ff:ff:ff",str(constants.DEVICE_NAME))


