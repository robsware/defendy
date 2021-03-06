from datetime import datetime
import flask
from flask import request
import os
import pandas as pd
import requests
import subprocess
import sys
import time
import re

app = flask.Flask(__name__)

#set current folder as main folder
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)



@app.route('/rename', methods=['GET'])

def renameAPI():
	oldDeviceName = request.args.get('oldName', default = 1, type = str)
	newDeviceName = request.args.get('newName', default = 1, type = str)
	#print (oldDeviceName)
	#print (newDeviceName)
	oldDeviceName = oldDeviceName.split(" ", 1)[1]
	with open('namedDevices.txt') as f:
		namedDevices = f.readlines()
		for num, line in enumerate(namedDevices, 1):
			if oldDeviceName in line:
				line = line.replace(oldDeviceName, newDeviceName)
				#print (namedDevices[num-1])
				namedDevices[num-1] = line
				#print (namedDevices[num-1])

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

@app.route('/remove', methods=['GET'])
def removeAPI():
	removeDeviceName = request.args.get('removeName', default = 1, type = str)

	IPToPurge = removeDeviceName.split(" ", 1)[0]
	removeDeviceName = removeDeviceName.split(" ", 1)[1]
	with open('namedDevices.txt') as f:
		namedDevices = f.readlines()
		for num, line in enumerate(namedDevices, 1):
			if removeDeviceName in line:
				namedDevices.remove(namedDevices[num-1])


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


	os.remove("../../machinelearning/IPTablesRules_" + IPToPurge)
	subprocess.call("../../firewall.sh", shell=True)


	for rulesFile in os.listdir('../../machinelearning'):
		if re.match('IPTablesRules_', rulesFile):
			with open (rulesFile, 'r') as rulesFileContent:
				lines = rulesFileContent.readlines()
				for line in lines:
					os.system(line)

	with open('/var/log/suricata/eve.json') as oldfile, open('../../machinelearning/eve_new.json', 'w') as newfile:
		for line in oldfile:
			if IPToPurge not in line:
				newfile.write(line)

	os.remove('/var/log/suricata/eve.json')
	os.rename('/var/log/suricata/eve_new.json', '/var/log/suricata/eve.json')
	
	return("Devices removed successfully")

@app.route('/reset', methods=['GET'])
def resetAPI():
	resetDeviceName = request.args.get('resetName', default = 1, type = str)


	resetDeviceIP = resetDeviceName.split(" ", 1)[0]
	#print (resetDeviceName.split(" ", 1)[1])
	#print (resetDeviceIP)
	os.remove("../../machinelearning/IPTablesRules_" + resetDeviceIP)

	subprocess.call("../../firewall.sh", shell=True)


	for rulesFile in os.listdir('../../machinelearning'):
		if re.match('IPTablesRules_', rulesFile):
			with open (rulesFile, 'r') as rulesFileContent:
				lines = rulesFileContent.readlines()
				for line in lines:
					os.system(line)

	with open('/var/log/suricata/eve.json') as oldfile, open('../../machinelearning/eve_new.json', 'w') as newfile:
		for line in oldfile:
			if resetDeviceIP not in line:
				newfile.write(line)

	os.remove('/var/log/suricata/eve.json')
	os.rename('/var/log/suricata/eve_new.json', '/var/log/suricata/eve.json')

	return("Firewall rules reset")


@app.route('/resetInbound', methods=['GET'])
def resetInboundAPI():
	os.remove("../../machinelearning/InboundIPTablesRles")


	subprocess.call("../../firewall.sh", shell=True)


	for rulesFile in os.listdir('../../machinelearning'):
		if re.match('IPTablesRules_', rulesFile):
			with open (rulesFile, 'r') as rulesFileContent:
				lines = rulesFileContent.readlines()
				for line in lines:
					os.system(line)




	return("Inbound firewall rules reset")

'''
@app.route('/scan', methods=['GET'])
def my_route2():



	return("Scanning..")
'''

app.run(host="10.10.0.1")
