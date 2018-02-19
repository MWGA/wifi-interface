# wifi-interface
This program interacsts with the 802.11 NIC and forwards 802.11 frames to OVS

####Requirements:
* scapy - python library
* WiFi interface with monitor mode support

####Content:
* constants.py - contains constants used in project
* createVethPair.sh - bash script to create virtual interfaces that communicate with OVS
* receiveProcess.py - process that receives 802.11 frames, encapsulate them into Ethernet and sends to OVS
* sendBeacons.py - process that sends beacon frames in certain intervals
* sendProbeRequest.py - script for creating and sending Probe requests
* sendProbeResponse.py - process that respond to Probe requests
* sendProcess.py - process that receives frames from OVS and sends them via 802.11