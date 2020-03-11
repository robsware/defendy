from sklearn.ensemble import IsolationForest
import numpy as np
import csv
import matplotlib.pyplot as pp

portData=[]
tempList = []
with open('outbound_10.10.0.100.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        try:
            tempList.append(row[1])
            tempList.append(row[3])
            portData.append(tempList)
            tempList = []
        except:
            print (row)

print ("stop")

portData.remove('10.10.0.100')

#convert to int
portData = list(map(int, portData))
result = [i for i in portData if i.startswith('10.10')]

val = 0 # this is the value where you want the data to appear on the y-axis.
pp.plot(portData, np.zeros_like(portData) + val, 'x')
pp.show()

#np.random.seed(1)
#random_data = np.random.randn(50000,2)  * 20 + 20

clf = IsolationForest( behaviour = 'new', max_samples=100, random_state = 1, contamination= 'auto')
preds = clf.fit_predict(portData)
preds