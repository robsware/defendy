#IP list of connected devices
import json
import re
ipList = []

with open('namedDevices.txt') as f:
	for line in f.readlines():
		ipList.append(line.split("\t")[0])
	print (ipList)


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

print ("done")


#Data cleanup

outboundList = [i for i in deviceActivity if i[0].startswith('10.10')]
inboundList = [i for i in deviceActivity if not i[0].startswith('10.10')]
inboundList = [ i for i in inboundList if "0.0.0.0" not in i ]


j = 0
for element in deviceActivity:
	print (deviceActivity[j][0])
	j += 1


