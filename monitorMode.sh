#!/bin/bash

if [[ $EUID > 0 ]]; then 
  echo "Please run as root/sudo"
  exit 1
else
  ifconfig wlx98ded0056388 down
  iwconfig wlx98ded0056388 mode monitor
  ifconfig wlx98ded0056388 up
fi
