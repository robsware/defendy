# defendy
An easy to deploy access point for your untrusted IoT devices. The software comes with a number of ready to deploy defences, such as blocking any traffic between the devices on the network except SSH, blocking most currently known internet scanners (SHODAN, Censys), an IDS through suricata, as well as a web interface where you can track, rename and remove your devices which can be accessed by connection to the access point and accessing 10.10.0.1. Designed to run on most development boards, with less than 500 MBs of RAM. Tested on a raspberryPi 3a and 3b+ with an USB antenna.

## Requirements
suricata
hostapd
python3 and the libraries in requirements.txt

The default broadcast interface is wlan1, can be changed by running install.sh from the main directory

## Running

Once the setup is complete, execute 

```
run.sh
```

from the main directory as sudo. You may now connect your devices to the access point.

## Experimental Features
** These features have not been tested, but should work.**

There is a machine learning IPS module that is deactivated by default, as it is too demanding for a raspberry Pi.

install.sh should install the necessary prerequisites
Run with -IPS for install the IPS version

To run Defendy with a machine learning based IPS, execute run.sh with the -IPS flag