#IP list of connected devices
#generates a file with all the traffic captured by suricata
import json
import re
import csv
import os
from sklearn.ensemble import IsolationForest
import numpy as np
import matplotlib.pyplot as pp
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
from datetime import datetime
import time



#set location directory as working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def createInboundandOutboundFiles():
#get the IP from all connected devices
	ipList = []
	with open('../../webpage/textdata/namedDevices.txt') as f:
		for line in f.readlines():
			ipList.append(line.split("\t")[0])

	#get source IP, port, destination IP and destination port
	ipPattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
	deviceActivity = []
	ports = []
	data = [json.loads(line) for line in open('/var/log/suricata/eve.json', 'r')]
	i = 0
	for ip in ipList:
		for line in data:
			try:
				ports.append(data[i]['src_ip'])
				ports.append(data[i]['src_port'])
				ports.append(data[i]['dest_ip'])
				ports.append(data[i]['dest_port'])
				#remove IPv6 and empty entries
				if ipPattern.match(ports[0]):
					deviceActivity.append(ports)
					ports = []
				else:
					ports = []
			except Exception:
				pass

			i += 1


	#Data cleanup
	outboundList = [i for i in deviceActivity if i[0].startswith('10.10')]
	inboundList = [i for i in deviceActivity if not i[0].startswith('10.10')]
	inboundList = [ i for i in inboundList if "0.0.0.0" not in i ]

	#remove router traffic
	outboundList = [i for i in outboundList if i[0] != '10.10.0.1']
	inboundList = [i for i in inboundList if i[2] != '10.10.0.1']

	#separate by device IP
	#let it be known I tried to use a lambda and I kept running into some weird bugs
	#deviceConnections = [i for i in outboundList if i[0] == ip]
	deviceConnections = []
	for ip in ipList:
		for i in outboundList:
			if i[0] == ip:
				deviceConnections.append(i)

		with open('outbound_' + ip +'.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(deviceConnections)
		deviceConnections = []

	for ip in ipList:
		for i in inboundList:
			if i[2] == ip:
				deviceConnections.append(i)

		with open('inbound_' + ip +'.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(deviceConnections)
		deviceConnections = []

	return()




def createBaseline(ip):
	#check if baseline already exists
	

	#data for ML
	#check if there is data
	if os.stat('outbound_' + ip + '.csv').st_size == 0:
		return()
	trafficData = pd.read_csv('outbound_' + ip + '.csv', names=["srcIP", "srcPort", "dstIP", "dstPort"]) 
	#encode source IP
	values = np.array(trafficData['srcIP'])
	integer_encoded = LabelEncoder().fit_transform(values)
	trafficData['intEncodedSourceIP'] = integer_encoded
	#encode destination IP
	values = np.array(trafficData['dstIP'])
	integer_encoded = LabelEncoder().fit_transform(values)
	trafficData['intEncodedDestIP'] = integer_encoded

	#training
	isolationForest = IsolationForest(behaviour='deprecated', bootstrap=False, contamination=0, max_features=1.0, max_samples='auto', n_estimators=100, n_jobs=None, random_state=None, verbose=0, warm_start=False)
	relevantCols = trafficData[["intEncodedSourceIP", "srcPort", "intEncodedDestIP", "dstPort"]]
	isolationForest.fit(relevantCols)
	pickle.dump(isolationForest, open('outboundTrained_' + ip + '.sav', 'wb'))



	if os.stat('inbound_' + ip + '.csv').st_size == 0:
		return()

	trafficData = pd.read_csv('inbound_' + ip + '.csv', names=["srcIP", "srcPort", "dstIP", "dstPort"]) 
	#encode source IP
	values = np.array(trafficData['srcIP'])
	integer_encoded = LabelEncoder().fit_transform(values)
	trafficData['intEncodedSourceIP'] = integer_encoded
	#encode destination IP
	values = np.array(trafficData['dstIP'])
	integer_encoded = LabelEncoder().fit_transform(values)
	trafficData['intEncodedDestIP'] = integer_encoded

	#training
	isolationForest = IsolationForest(behaviour='deprecated', bootstrap=False, contamination=0, max_features=1.0, max_samples='auto', n_estimators=100, n_jobs=None, random_state=None, verbose=0, warm_start=False)
	relevantCols = trafficData[["intEncodedSourceIP", "srcPort", "intEncodedDestIP", "dstPort"]]
	isolationForest.fit(relevantCols)
	pickle.dump(isolationForest, open('inboundTrained_' + ip + '.sav', 'wb'))



	return()





def loadModel(ip):
	try:
		loaded_model = pickle.load(open('outboundTrained_' + ip + '.sav', 'rb'))
	except:
		print ("bad")
		return()
	newTrafficData = pd.read_csv('new_' + ip + '.csv', names=["srcIP", "srcPort", "dstIP", "dstPort"]) 
	#encode source IP
	values = np.array(newTrafficData['srcIP'])
	integer_encoded = LabelEncoder().fit_transform(values)
	newTrafficData['intEncodedSourceIP'] = integer_encoded
	#encode destination IP
	values = np.array(newTrafficData['dstIP'])
	integer_encoded = LabelEncoder().fit_transform(values)
	newTrafficData['intEncodedDestIP'] = integer_encoded
	newCols = newTrafficData[["intEncodedSourceIP", "srcPort", "intEncodedDestIP", "dstPort"]]
	pred = loaded_model.predict(newCols)
	newTrafficData['anomaly']=pred
	print (pred)
	outliers=newTrafficData.loc[newTrafficData['anomaly']==-1]
	outliers[["srcIP", "srcPort", "dstIP", "dstPort"]].to_csv("outboundOutliers_" + ip + ".csv", index=None)



	try:
		loaded_model = pickle.load(open('inboundTrained_' + ip + '.sav', 'rb'))
	except:
		print ("bad")
		return()
	newTrafficData = pd.read_csv('new_' + ip + '.csv', names=["srcIP", "srcPort", "dstIP", "dstPort"]) 
	#encode source IP
	values = np.array(newTrafficData['srcIP'])
	integer_encoded = LabelEncoder().fit_transform(values)
	newTrafficData['intEncodedSourceIP'] = integer_encoded
	#encode destination IP
	values = np.array(newTrafficData['dstIP'])
	integer_encoded = LabelEncoder().fit_transform(values)
	newTrafficData['intEncodedDestIP'] = integer_encoded
	newCols = newTrafficData[["intEncodedSourceIP", "srcPort", "intEncodedDestIP", "dstPort"]]
	pred = loaded_model.predict(newCols)
	newTrafficData['anomaly']=pred
	print (pred)
	outliers=newTrafficData.loc[newTrafficData['anomaly']==-1]
	outliers[["srcIP", "srcPort", "dstIP", "dstPort"]].to_csv("inboundOutliers_" + ip + ".csv", index=None)



	return ()



def generateFWRules():
	for outliersFile in os.listdir('.'):
		if re.match('outboundOutliers', outliersFile):
			IPForFiltering = outliersFile.split('_')[1]
			IPForFiltering = IPForFiltering.split('.csv')[0]
			outliersFileContent = pd.read_csv(outliersFile, names=["srcIP", "srcPort", "dstIP", "dstPort"])
			print (outliersFileContent)
			rowsFilteredByIP = outliersFileContent[outliersFileContent['srcIP'].str.match(IPForFiltering)]
			print (rowsFilteredByIP)
			for index, row in rowsFilteredByIP.iterrows():
				with open("outboundIPTablesRules" + IPForFiltering, 'a') as IPTablesRulesFile:
					IPTablesRulesFile.write("iptables -A OUTPUT -p tcp -d " + row['srcIP'] + " --destination-port " + str(row['srcPort']) + " -j DROP" + '\n')

					#os.system("iptables -A OUTPUT -p tcp -d " + row['srcIP'] + " --destination-port " + str(row['srcPort']) + " -j DROP")
					#print("iptables -A OUTPUT -p tcp -d " + row['srcIP'] + " --destination-port " + str(row['srcPort']) + " -j DROP")


		if re.match('inboundOutliers', outliersFile):

			outliersFileContent = pd.read_csv(outliersFile, names=["srcIP", "srcPort", "dstIP", "dstPort"])
			print (outliersFileContent)			
			for index, row in outliersFileContent.iterrows():
				with open("InboundIPTablesRles", 'a') as inboundTablesRulesFile:
					inboundTablesRulesFile.write("iptables -A INPUT -p tcp --destination-port " + str(row['srcPort']) +  " -s " + row['srcIP'] +" -j DROP")
					#print ("iptables -A INPUT -p tcp --destination-port " + str(row['srcPort']) +  " -s " + row['srcIP'] +" -j DROP")


	return()


def applyFWrules():

	#load rules in iptables
	try:
		for rulesFile in os.listdir('.'):
			if re.match('outboundIPTablesRules', rulesFile):
				with open (rulesFile, 'r') as rulesFileContent:
					lines = rulesFileContent.readlines()
					for line in lines:
						#print (line)
						os.system(line)
	except:
		pass
			

	try:			
		with open ("InboundIPTablesRles", 'r') as inboundRulesFile:
			inboundRulesLines = inboundRulesFile.readlines()
			for line in inboundRulesLines:
				print (line)
				os.system(line)
	except:
		pass
	return()







while True:
	with open('../../webpage/textdata/namedDevices.txt') as f:
		for line in f.readlines():
			ip = line.split("\t")[0]
			try:
				loadModel(ip)
			except:
				pass
	applyFWrules()

	#list of IPs
	with open('../../webpage/textdata/namedDevices.txt') as f:
		for line in f.readlines():
			ip = line.split("\t")[0]
			date = line.split("\t")[3]
			date = date.strip()
			date = datetime.strptime(date, '%Y-%m-%d')
			today = date.today()
			delta = today - date
			if delta.days > 30:
				createBaseline(ip)

	time.sleep(3600)

