from sklearn.ensemble import IsolationForest
import numpy as np
import csv
import matplotlib.pyplot as pp
import pandas as pd
from sklearn.preprocessing import LabelEncoder


trafficData = pd.read_csv('outbound_10.10.0.100.csv', names=["srcIP", "srcPort", "dstIP", "dstPort"]) 



print ("stop")

#encoding source IP
data = trafficData['srcIP']
values = np.array(data)

label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
trafficData['intEncodedSourceIP'] = integer_encoded

#encoding destination IP
data = trafficData['dstIP']
values = np.array(data)

integer_encoded = label_encoder.fit_transform(values)
trafficData['intEncodedDestIP'] = integer_encoded

#relevantCols = relevantCols.astype(int)
#testdf = relevantCols[~relevantCols.applymap(np.isreal).all(1)]


#training
iForest = IsolationForest(behaviour='deprecated', bootstrap=False, contamination=0, max_features=1.0, max_samples='auto', n_estimators=100, n_jobs=None, random_state=None, verbose=0, warm_start=False)
relevantCols = trafficData[["intEncodedSourceIP", "srcPort", "intEncodedDestIP", "dstPort"]]
iForest.fit(relevantCols)


portData.remove('10.10.0.100')


newTrafficData = pd.read_csv('contaminated_10.10.0.100.csv', names=["srcIP", "srcPort", "dstIP", "dstPort"]) 

data = newTrafficData['srcIP']
values = np.array(data)

label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
newTrafficData['intEncodedSourceIP'] = integer_encoded

#encoding destination IP
data = newTrafficData['dstIP']
values = np.array(data)

integer_encoded = label_encoder.fit_transform(values)
newTrafficData['intEncodedDestIP'] = integer_encoded


newiForest = IsolationForest(behaviour='deprecated', bootstrap=False, contamination=0.1, max_features=1.0, max_samples='auto', n_estimators=100, n_jobs=None, random_state=None, verbose=0, warm_start=False)
newCols = newTrafficData[["intEncodedSourceIP", "srcPort", "intEncodedDestIP", "dstPort"]]
newTrafficData['anomaly'] = ""
pred = newiForest.predict(newCols)
newTrafficData['anomaly']=pred
outliers=newTrafficData.loc[newTrafficData['anomaly']==-1]

#convert to int
#portData = list(map(int, portData))
#result = [i for i in portData if i.startswith('10.10')]


#np.random.seed(1)
#random_data = np.random.randn(50000,2)  * 20 + 20

clf = IsolationForest( behaviour = 'new', max_samples=100, random_state = 1, contamination= 'auto')
preds = clf.fit_predict(portData)
preds