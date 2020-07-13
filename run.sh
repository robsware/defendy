newInterface=$(cat hostapd.conf | grep wlan | cut -f2 -d"=")
echo $newInterface


sudo ifdown $newInterface
sudo ifup $newInterface
sudo service hostapd restart

sudo suricata -c /etc/suricata/suricata.yaml -i $newInterface

#TODO: add sudo and port 80
python3 -m http.server --directory webpage/

python3 webpage/textdata/renameDevice.py

