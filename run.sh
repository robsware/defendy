newInterface=$(cat hostapd.conf | grep wlan | cut -f2 -d"=")
echo $newInterface


sudo ifdown $newInterface
sudo ifup $newInterface
sudo service hostapd restart

sudo bash firewall.sh

python3 -m http.server --directory webpage/ 80&

sudo python3 webpage/textdata/statusCheck.py &

python3 webpage/textdata/renameDevice.py &

python3 machinelearning/IPS.py &

sudo suricata -c /etc/suricata/suricata.yaml -i $newInterface -D