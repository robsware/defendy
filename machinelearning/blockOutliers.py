import os
import re
import pandas as pd


for outliersFile in os.listdir('.'):
   if re.match('outliers', outliersFile):
       IPForFiltering = outliersFile.split('_')[1]
       IPForFiltering = IPForFiltering.split('.csv')[0]
       outliersFileContent = pd.read_csv(outliersFile) 
       print (outliersFileContent)
       fieldsFilteredByIP = outliersFileContent[outliersFileContent['srcIP'].str.match(IPForFiltering)]
       print (fieldsFilteredByIP)
       for index, row in fieldsFilteredByIP.iterrows():
           #with open("IPTablesRules_" + IPForFiltering, 'w'):
           #print(row['srcIP'], row['srcPort'])
           print("iptables -A OUTPUT -p tcp -d " + row['srcIP'] + " --destination-port " + str(row['srcPort']) + " -j DROP")
            
           #print(row['srcIP'], row['srcPort'])

       


       #fieldsFilteredByIP[["srcIP", "srcPort", "dstIP", "dstPort"]].to_csv("ipTablesRules_" + ip + ".csv", index=None)





'''
for file starting with outliers in name:
    with open outliers

        if srcIp is 10.10.something:
            block outbound on srcIp and srcPort
        elif srcIp is not 10.10.something:
            block inbound on srcIp and srcPort
        

Create file with new outbound rules
Match ip and add button to remove all rules related to that ip


Add any new inbound rules to a file (like the deny scanners one)
Button to reset inbount rules (delete that file)


for ip in ips:
    os.system("iptables -A INPUT -j DROP -s " + ip)
    os.system("iptables -A INPUT -j DROP -s " + ip)
    # iptables -A OUTPUT -p tcp -d 10.10.10.10 --destination-port 25 -j DROP
    # iptables -A INPUT -p tcp --destination-port 8000 -s 1.2.3.4 -j DROP
'''