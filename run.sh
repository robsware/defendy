newInterface=$(cat hostapd.conf | grep wlan | cut -f2 -d"=")
echo $newInterface


sudo ifdown $newInterface
sudo ifup $newInterface
sudo service hostapd restart

sudo firewall.sh

#TODO: add sudo and port 80
nohup python3 -m http.server --directory webpage/ 80&

nohup python3 webpage/textdata/renameDevice.py &

sudo suricata -c /etc/suricata/suricata.yaml -i $newInterface -D