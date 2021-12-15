#!/bin/sh

PACKAGES="python3-pip"
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install $PACKAGES -y
sudo pip3 install adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
echo "Install complete, rebooting"
reboot


