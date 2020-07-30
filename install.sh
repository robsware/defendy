#!/bin/bash

#sudo apt-get install hostapd
#sudo apt-get install suricata
#sudo cp hostapd.conf /etc/hostapd/hostapd.conf
#sudo cp interfaces /etc/network/interfaces


echo "Default broadcast interface is set on wlan1. Change? yes/no"
read changeInterface
if [[ $changeInterface == "yes" ]] || [[ $changeInterface == "y" ]];
then
	echo "Input new interface. Example: wlan0"
	read newInterface
	sed -i "s/wlan1/$newInterface/g" hostapd.conf
	sed -i "s/wlan1/$newInterface/g" interfaces
	sed -i "s/wlan1/$newInterface/g" webpage/textdata/renameDevice.py
	sed -i "s/wlan1/$newInterface/g" webpage/textdata/statusCheck.py
else
	echo "Keeping original interface, wlan1"
	newInterface=wlan1

fi

echo "Please enter a password for the wifi network:"
read newPassword
sed -i "s/securepass/$newPassword/g" hostapd.conf


sudo pip3 install -r requirements.txt


echo "Done"