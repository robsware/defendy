from datetime import datetime
import os
import requests
import subprocess
import sys
import time

def checkAlerts():
	with open('/var/log/suricata/fast.log') as f:
	#with open('fast.log') as f:
		alerts = f.readlines()
		with open ('fast_prio.log', 'w') as wf:
			for line in alerts:
				if '[Priority: 1]' in line or '[Priority: 2]' in line:
					#line = line.split('{TCP} ')[1]
					#line = line.split(' ')[0]
					wf.write(line)
	return()


def detectDevices():
	string="iw wlan1 station dump | grep Station"
	result=subprocess.getoutput(string)
	try:
		macAddr = result.split(" ")[1]
		with open('knownDevices.txt') as f:
			knownDevices = f.readlines()
			if macAddr not in knownDevices:
				with open("knownDevices.txt", "w") as file:
					file.write(macAddr + "\n")
	except:
		print("No devices connected yet")


	arpScan="sudo arp-scan --interface=wlan1 --localnet"
	allDevices=subprocess.getoutput(arpScan)
	listAllDevices = allDevices.splitlines()


	for element in listAllDevices:
		try:
			if macAddr in element:
				print ("Device connected: ", element)
				with open('namedDevices.txt') as f:
					namedDevices = f.readlines()
					if element not in namedDevices:
						with open("namedDevices.txt", "w") as file:
							file.write(element + "\t"+ datetime.today().strftime('%Y-%m-%d'))

		except:
			pass
	return()


def getPublicIP():
	publicIP = requests.get('http://ifconfig.me')

	publicIP = publicIP.content
	publicIP = publicIP.decode("utf-8") 


	with open("publicIP.txt", "w") as f:
	    f.writelines(publicIP)



while True:
	checkAlerts()
	detectDevices()
	getPublicIP()
	time.sleep(15)