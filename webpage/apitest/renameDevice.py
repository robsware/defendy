import sys

print ("Known Devices: ")

with open('namedDevices.txt') as f:
	namedDevices = f.readlines()
	i = 1
	for name in namedDevices:
		print (str(i) + ". " + name)
		i += 1

#deviceNumber = input("Select a device to rename: ")
deviceNumber = sys.argv[1]
deviceNumber = int(deviceNumber) - 1

newDeviceName = sys.argv[2]

with open('namedDevices.txt') as f:
	namedDevices = f.readlines()
	deviceToRename = namedDevices[deviceNumber]
	deviceName = deviceToRename.split("\t")[2]
	deviceToRename = deviceToRename.replace(deviceName, newDeviceName)
	namedDevices[deviceNumber] = deviceToRename

with open('namedDevices.txt', 'w') as f:
	f.writelines(namedDevices)
