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


del displayDF["MAC Address"]
displayDF.to_csv('renameDevices.txt', sep='\t', index=False, header=False)
