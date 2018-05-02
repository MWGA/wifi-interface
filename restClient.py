import requests

import constants

url = 'http://localhost:5000/lvap'


def generate_lvap(mac, wtp):
    response = requests.post(url, json={
        "ip": "192.168.0.1",
        "mac": mac,
        "bssid": "ff:ff:ff:ff:ff:ff",
        "ssid": constants.SSID,
        "wtp": wtp
    })

    print(response.json())
