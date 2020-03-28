import sys
import flask
import os 
from flask import request
import pandas as pd

app = flask.Flask(__name__)



@app.route('/rename', methods=['GET'])

def my_route():
  oldDeviceName = request.args.get('oldName', default = 1, type = str)
  newDeviceName = request.args.get('newName', default = 1, type = str)
  print (oldDeviceName)
  print (newDeviceName)
  oldDeviceName = oldDeviceName.split(" ")[1]
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

  print ("stop")

  with open("displayDevices.txt") as f:
	  lines = f.readlines()
	  lines[0] = "\t" + "IP Address" + "\t" + "MAC Address" + "\t" + "\t" +"Name" + "\n"

  with open("displayDevices.txt", "w") as f:
	  f.writelines('<option>' + lines + '</option>')


  del displayDF["MAC Address"]
  displayDF.to_csv('renameDevices.txt', sep='\t', index=False, header=False)

  return("Ok")

app.run()

