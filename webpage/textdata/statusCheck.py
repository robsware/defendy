from datetime import datetime
import os
import requests
import subprocess
import sys
import time
import pandas as pd

def detectDevices():
	string="iw wlan1 station dump | grep Station"
	result=subprocess.getoutput(string)
	for line in result.splitlines():
		try:
			macAddr = line.split(" ")[1]
			with open('knownDevices.txt') as f:
				knownDevices = f.readlines()
				if macAddr+'\n' not in knownDevices:
					with open("knownDevices.txt", "a") as file:
						file.write(macAddr + "\n")
		except:
			print("No new devices connected yet")
	return()


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
	
	
	displayDF = pd.read_csv('namedDevices.txt', names=["IP Address","MAC Address","Name","Date Added"], sep='\t')

	displayDF.index += 1 
	del displayDF["Date Added"]

	displayDF.to_csv('displayDevices.txt', sep='\t')

	with open("displayDevices.txt") as f:
		lines = f.readlines()
		lines[0] = "\t" + "IP Address" + "\t" + "MAC Address" + "\t" + "\t" +"Name" + "\n"

	with open("displayDevices.txt", "w") as f:
		f.writelines(lines)
	

	del displayDF["MAC Address"]
	displayDF.to_csv('renameDevices.txt', sep='\t', index=False, header=False)

	with open("renameDevices.txt") as f:
		lines = f.readlines()
		lines = [line + '</option>' for line in lines]
		lines = ['<option>' + line  for line in lines]


	with open("renameDevices.txt", "w") as f:
		f.writelines(lines)

	return()

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

def getPublicIP():
	publicIP = requests.get('http://ifconfig.me')

	publicIP = publicIP.content
	publicIP = publicIP.decode("utf-8") 


	with open("publicIP.txt", "w") as f:
	    f.writelines(publicIP)
	return()



while True:
	detectDevices()
	checkAlerts()
	getPublicIP()
	time.sleep(20)
