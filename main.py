#!/usr/bin/python

import threading

import packetHandlerFromWiFi
import sendBeacons

t1 = threading.Thread(name='WTP', target=packetHandlerFromWiFi.start())
t2 = threading.Thread(name='Beacons', target=sendBeacons.transmitBeacons())

t1.start()
t2.start()
