from sklearn.ensemble import IsolationForest
import numpy as np
import csv
import matplotlib.pyplot as pp
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

#TODO: add a check so that it doesn't create a new baseline for devices that already have one
#TODO: add a check against empty files

def createBaseline(ip):
	#data for ML
	trafficData = pd.read_csv('inbound_' + ip + '.csv', names=["srcIP", "srcPort", "dstIP", "dstPort"]) 
	print (trafficData)
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
	pickle.dump(isolationForest, open("trained_" + ip + '.sav', 'wb'))

	return()


#relevantCols = relevantCols.astype(int)
#testdf = relevantCols[~relevantCols.applymap(np.isreal).all(1)]


#list of IPs
with open('namedDevices.txt') as f:
	for line in f.readlines():
		ip = line.split("\t")[0]
		print (ip)
		createBaseline(ip)



########################################################
#y_pred_train = isolationForest.predict(relevantCols)




