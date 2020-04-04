#write out current crontab
crontab -l > mycron
#echo new cron into cron file

echo "* * * * * python3 /opt/defendy/webpage/python/getPublicIP.py" >> mycron
echo "* * * * * python3 /opt/defendy/webpage/python/detect-devices.py" >> mycron
echo "* * * * * python3 /opt/defendy/webpage/python/checkAlerts.py" >> mycron
echo "* * * * * python3 /opt/defendy/webpage/textdata/renameDevice.py" >> mycron
echo "* * * * * bash /opt/defendy/webpage/firewall.sh" >> mycron


#install new cron file
crontab mycron
rm mycron