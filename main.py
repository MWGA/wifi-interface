#!/usr/bin/python

import threading

import probeProcess

t1 = threading.Thread(name='WTP', target=probeProcess.start())
# t2 = threading.Thread(name='LDAP', target=worker)

t1.start()
