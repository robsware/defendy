import pandas as pd
import os
os.chdir("webpage")

displayDF = pd.read_csv('namedDevices.txt', names=["IP Address","MAC Address","Name","Date Added"], sep='\t')

displayDF.index += 1 
del displayDF["Date Added"]

displayDF.to_csv('displayDevices.txt', sep='\t')

print ("stop")

with open("displayDevices.txt") as f:
    lines = f.readlines()
    lines[0] = "\t" + "IP Address" + "\t" + "MAC Address" + "\t" + "\t" +"Name" + "\n"

with open("displayDevices.txt", "w") as f:
    f.writelines(lines)



with open('index.html','r') as file:
    filedata = file.read()
    filedata = filedata.replace('test.js?q=','test.js?q=13512')
with open('index.html','w') as file:
    file.write(filedata)