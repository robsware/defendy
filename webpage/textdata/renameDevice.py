from datetime import datetime
import flask
from flask import request
import iptc
import os
import pandas as pd
import requests
import subprocess
import sys
import time

app = flask.Flask(__name__)

#set current folder as main folder
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)



@app.route('/rename', methods=['GET'])

def my_route():
	oldDeviceName = request.args.get('oldName', default = 1, type = str)
	newDeviceName = request.args.get('newName', default = 1, type = str)
	print (oldDeviceName)
	print (newDeviceName)
	oldDeviceName = oldDeviceName.split(" ", 1)[1]
	with open('namedDevices.txt') as f:
		namedDevices = f.readlines()
		for num, line in enumerate(namedDevices, 1):
			if oldDeviceName in line:
				line = line.replace(oldDeviceName, newDeviceName)
				print (namedDevices[num-1])
				namedDevices[num-1] = line
				print (namedDevices[num-1])

	with open('namedDevices.txt', 'w') as f:
		f.writelines(namedDevices)

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




	return("Device renamed successfully")

@app.route('/update', methods=['GET'])
def my_route1():
	x = 1
	x = x + 1
	return(str(x))


@app.route('/scan', methods=['GET'])
def my_route2():



	return("Scanning..")

app.run()


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

'''
echo "* * * * * python3 /opt/defendy/webpage/python/getPublicIP.py" >> mycron
echo "* * * * * python3 /opt/defendy/webpage/python/detect-devices.py" >> mycron
echo "* * * * * python3 /opt/defendy/webpage/python/checkAlerts.py" >> mycron
'''