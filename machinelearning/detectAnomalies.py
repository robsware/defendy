from sklearn.ensemble import IsolationForest
import numpy as np
import csv
import matplotlib.pyplot as pp
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
import os

#set location directory as working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def loadModel(ip):
	try:
		loaded_model = pickle.load(open('trained_' + ip + '.sav', 'rb'))
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
	outliers[["srcIP", "srcPort", "dstIP", "dstPort"]].to_csv("outliers_" + ip + ".csv", index=None)
	return ()


with open('namedDevices.txt') as f:
	for line in f.readlines():
		ip = line.split("\t")[0]
		loadModel(ip)

