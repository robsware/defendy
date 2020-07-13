#!/bin/bash
echo "Default broadcast interface is set on wlan1. Change? yes/no"
read changeInterface
if [[ $changeInterface == "yes" ]] || [[ $changeInterface == "y" ]];
then
	echo "Input new interface. Example: wlan0"
	read newInterface
	sed -i "s/wlan1/$newInterface/g" hostapd.conf
	sed -i "s/wlan1/$newInterface/g" interfaces
else
	echo "Keeping original interface, wlan1"
	newInterface=wlan1

fi


#sudo apt-get install hostapd
#sudo apt-get install suricata
#sudo cp hostapd.conf /etc/hostapd/hostapd.conf
#sudo cp interfaces /etc/network/interfaces




echo "Done"