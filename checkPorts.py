#IP list of connected devices
import json
import re
import csv
ipList = []

with open('namedDevices.txt') as f:
	for line in f.readlines():
		ipList.append(line.split("\t")[0])
	print (ipList)


ipPattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
deviceActivity = []
ports = []
data = [json.loads(line) for line in open('eve.json', 'r')]
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

print ("done")


#Data cleanup

outboundList = [i for i in deviceActivity if i[0].startswith('10.10')]
inboundList = [i for i in deviceActivity if not i[0].startswith('10.10')]
inboundList = [ i for i in inboundList if "0.0.0.0" not in i ]

outboundList = [i for i in outboundList if i[0] != '10.10.0.1']
inboundList = [i for i in inboundList if i[2] != '10.10.0.1']

#separate by IP
deviceConnections = []
for ip in ipList:
	for i in outboundList:
		if i[0] == ip:
			deviceConnections.append(i)
	print (deviceConnections)
	with open('outbound_' + ip +'.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(deviceConnections)
	deviceConnections = []

for ip in ipList:
	for i in inboundList:
		if i[2] == ip:
			deviceConnections.append(i)
	print (deviceConnections)
	with open('inbound_' + ip +'.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(deviceConnections)
	deviceConnections = []




