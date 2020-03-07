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

#TODO: rename to outboundList after testing
cleanOutboundList = [i for i in outboundList if i[0] != '10.10.0.1']
cleanInboundList = [i for i in inboundList if i[2] != '10.10.0.1']

#separate by IP
for ip in ipList:
	for i in cleanOutboundList:
		if i[0] == ip:
			deviceOutboundConnections.append(i)
	print (deviceOutboundConnections)
	with open('outbound_' + ip +'.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(deviceOutboundConnections)
	deviceOutboundConnections = []

#TODO: create a function that generates a file with all the traffic of a device. Also write inbound and outbound traffic to a file



testip = '10.10.0.100'
device1list = [i for i in cleanOutboundList if i[0] == testip]
deviceoutlist = [i for i in outboundList if i[2] == testip]

j = 0
for element in deviceActivity:
	print (deviceActivity[j][0])
	j += 1


first_tuple_list = [tuple(lst) for lst in outboundList]
secnd_tuple_list = [tuple(lst) for lst in device1list]
temp3 = set(first_tuple_list) - set(secnd_tuple_list)