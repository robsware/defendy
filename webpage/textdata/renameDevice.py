import sys
import flask
import os 
from flask import request
import pandas as pd
import subprocess
import time
from datetime import datetime

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

