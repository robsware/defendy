import os
import re
import pandas as pd


for outliersFile in os.listdir('.'):
	if re.match('outliers', outliersFile):
		IPForFiltering = outliersFile.split('_')[1]
		IPForFiltering = IPForFiltering.split('.csv')[0]
		outliersFileContent = pd.read_csv(outliersFile)
		print (outliersFileContent)
		rowsFilteredByIP = outliersFileContent[outliersFileContent['srcIP'].str.match(IPForFiltering)]
		print (rowsFilteredByIP)
		for index, row in rowsFilteredByIP.iterrows():
			with open("IPTablesRules_" + IPForFiltering, 'a') as IPTablesRulesFile:
				#IPTablesRulesFile.write("iptables -A OUTPUT -p tcp -d " + row['srcIP'] + " --destination-port " + str(row['srcPort']) + " -j DROP" + '\n')

				#os.system("iptables -A OUTPUT -p tcp -d " + row['srcIP'] + " --destination-port " + str(row['srcPort']) + " -j DROP")
				print("iptables -A OUTPUT -p tcp -d " + row['srcIP'] + " --destination-port " + str(row['srcPort']) + " -j DROP")
		#Rows that do not match an internal IP and come from the outside
		rowsInboundBadTraffic = outliersFileContent[~outliersFileContent['srcIP'].str.match(IPForFiltering)]
		for index, row in rowsInboundBadTraffic.iterrows():
			with open("InboundIPTablesRles", 'a') as inboundTablesRulesFile:
				#inboundTablesRulesFile.write("iptables -A INPUT -p tcp --destination-port " + str(row['srcPort']) +  " -s " + row['srcIP'] +" -j DROP")
				print ("iptables -A INPUT -p tcp --destination-port " + str(row['srcPort']) +  " -s " + row['srcIP'] +" -j DROP")



#load rules in iptables
for rulesFile in os.listdir('.'):
	if re.match('IPTablesRules_', rulesFile):
		with open (rulesFile, 'r') as rulesFileContent:
			lines = rulesFileContent.readlines()
			for line in lines:
				print (line)
				#os.system(line)
		

		   
with open ("InboundIPTablesRles", 'r') as inboundRulesFile:
	inboundRulesLines = inboundRulesFile.readlines()
	for line in inboundRulesLines:
		print (line)
		#os.system(line)
	   




#TODO: when you remove a device, also delete iptables rules

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