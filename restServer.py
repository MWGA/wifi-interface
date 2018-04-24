#!flask/bin/python
import json

from flask import Flask, request, Response

from LVAP import LVAP

app = Flask(__name__)

lvap_context = []


@app.route('/lvap', methods=['POST'])
def add_to_lvap():
    if not request.json or not 'mac' in request.json or not 'ip' in request.json or not 'bssid' in request.json or not 'ssid' in request.json or not 'wtp' in request.json:
        return 400
    mydata = request.json
    lvap_context.append(
        LVAP(str(mydata.get("ip")), str(mydata.get("mac")), str(mydata.get("bssid")), str(mydata.get("ssid")),
             str(mydata.get("wtp"))))
    s = ""
    for lvap in lvap_context:
        s += lvap.to_json()
    print("POST " + s)
    data = json.dumps(s)
    tdata = (data.replace("}, {", "}\\\0{")).replace("\\", "")
    #        LOG.info("TDATA = " + tdata)
    return Response(response=(tdata.replace("\"[", "")).replace("]\"", "") + chr(0),
                    mimetype='application/json')  # Adding a \0 to the end of the


@app.route('/lvap', methods=['DELETE'])
def delete_from_lvap():
    for lvap in lvap_context:
        if request.json['mac'] == lvap.MACaddress:
            lvap_context.remove(lvap)
    s = ""
    for lvap in lvap_context:
        s += lvap.to_json()
    print("DELETE " + s)
    data = json.dumps(s)
    tdata = (data.replace("}, {", "}\\\0{")).replace("\\", "")
    #        LOG.info("TDATA = " + tdata)
    return Response(response=(tdata.replace("\"[", "")).replace("]\"", "") + chr(0),
                    mimetype='application/json')  # Adding a \0 to the end of the


@app.route('/lvap', methods=['GET'])
def get_from_lvap():
    s = ""
    for lvap in lvap_context:
        s += lvap.to_json()
    print("GET" + s)
    data = json.dumps(s)
    tdata = (data.replace("}, {", "}\\\0{")).replace("\\", "")
    #        LOG.info("TDATA = " + tdata)
    return Response(response=(tdata.replace("\"[", "")).replace("]\"", "") + chr(0),
                    mimetype='application/json')  # Adding a \0 to the end of the


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
