#!/bin/sh

PACKAGES="python3-pip git"
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install $PACKAGES -y
sudo pip3 install adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
cd
git clone https://github.com/Howchoo/pi-power-button.git
./pi-power-button/script/install
sed -i -e '$i python3 /home/pi/pi-music/main.py > /home/pi/pi-music/logs/main.log 2>&1 &\n' rc.local
echo "Install complete, rebooting"
reboot


