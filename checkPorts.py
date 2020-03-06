#IP list of connected devices
import json
import re
ipList = []

with open('namedDevices.txt') as f:
	for line in f.readlines():
		ipList.append(line.split("\t")[0])
	print (ipList)

#JSON
data = [json.loads(line) for line in open('eve.json', 'r')]
print (data[120]['src_port'])

ipPattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
deviceActivity = []
ports = []
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
'''
for ip in ipList:
	with open ('eve.json') as f:
		for line in f.readlines():
			if ip in line:
				#print (line.split(ip)[1][2:53])
				deviceActivity.append(line.split(ip)[1][2:60])

ipSourceList = [i for i in deviceActivity if i.startswith('"src_port"')]
ipDestinationList = [i for i in deviceActivity if i.startswith('"dest_port"')]
'''
print ("done")

#data = [json.loads(line) for line in open('eve.json', 'r')]
#print (data[120]['src_port'])
#"src_ip":"10.10.0.100","src_port":41798,"dest_ip":"68.232.34.217","dest_port":443


j = 0
for element in deviceActivity:
	print (deviceActivity[j][0])
	j += 1


