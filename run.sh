newInterface=$(cat hostapd.conf | grep wlan | cut -f2 -d"=")
echo $newInterface


sudo ifdown $newInterface
sudo ifup $newInterface
sudo service hostapd restart

sudo bash firewall.sh

nohup python3 -m http.server --directory webpage/ 80&

python3 webpage/textdata/statusCheck.py &

python3 webpage/textdata/renameDevice.py &

sudo suricata -c /etc/suricata/suricata.yaml -i $newInterface -D