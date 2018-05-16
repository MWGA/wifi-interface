#!/usr/bin/python

import threading

import packetHandlerFromWiFi
import sendBeacons
import restServer

class baconThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print "Starting " + self.name
      packetHandlerFromWiFi.start()
      print "Exiting " + self.name

class wtpThread(threading.Thread):
  def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

  def run(self):
      print "Starting " + self.name
      sendBeacons.transmitBeacons()
      print "Exiting " + self.name


class restThread(threading.Thread):
  def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

  def run(self):
      print "Starting " + self.name
      restServer.start()
      print "Exiting " + self.name


thread1 = baconThread(1, "bacon-Thread-1", 1)
thread2 = wtpThread(2, "wtp-Thread-2", 2)
thread3 = restThread(3, "rest-Thread-3", 3)

thread1.start()
thread2.start()
thread3.start()

print "Exiting Main Thread"
