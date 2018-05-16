#!/bin/bash

if [[ $EUID > 0 ]]; then 
  echo "Please run as root/sudo"
  exit 1
else
  ifconfig wlx004f81048a95 down
  iwconfig wlx004f81048a95 mode monitor
  ifconfig wlx004f81048a95 up
fi
