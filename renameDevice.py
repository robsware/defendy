import sys
import flask
import os 
from flask import request

app = flask.Flask(__name__)



@app.route('/rename', methods=['GET'])

def my_route():
  oldDeviceName = request.args.get('oldName', default = 1, type = str)
  newDeviceName = request.args.get('newName', default = 1, type = str)
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


  return("Ok")

app.run()

