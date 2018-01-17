#!/bin/bash

if [[ $EUID > 0 ]]; then 
  echo "Please run as root/sudo"
  exit 1
else
  ip link add veth0 type veth peer name veth1
  ifconfig veth0 up
  ifconfig veth1 up
fi

