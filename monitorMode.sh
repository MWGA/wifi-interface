#!/bin/bash

if [[ $EUID > 0 ]]; then 
  echo "Please run as root/sudo"
  exit 1
else
  sudo ifconfig $1 down
  sudo iwconfig $1 mode monitor
  sudo ifconfig $1 up
  sudo iwconfig $1 channel 10
fi
