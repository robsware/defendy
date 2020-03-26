import sys

print ("Known Devices: ")


#deviceNumber = input("Select a device to rename: ")
oldDeviceName = sys.argv[1]
oldDeviceName = oldDeviceName.split(" ")[1]
print (oldDeviceName)

newDeviceName = sys.argv[2]

with open('namedDevices.txt') as f:
	namedDevices = f.readlines()
	for num, line in enumerate(namedDevices, 1):
		if oldDeviceName in line:
			line = line.replace(oldDeviceName, newDeviceName)
			print (namedDevices[num-1])
			namedDevices[num-1] = line
			print (namedDevices[num-1])

with open('namedDevices.txt', 'w') as f:
	f.writelines(namedDevices)
