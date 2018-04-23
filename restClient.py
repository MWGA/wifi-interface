import requests
url = 'http://localhost:5000/lvap'

response = requests.post(url, json={
  "ip": "192.168.0.1",
  "mac": "ff:ff:ff:ff:ff:f2",
  "bssid": "ff:ff:ff:ff:ff:ff",
  "ssid": "paradne ssid",
  "wtp": "myComdsaap"
})

print(response.json())