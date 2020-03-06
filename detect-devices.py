import subprocess
import time



try:
    file = open('knownDevices.txt', 'r')
except IOError:
    file = open('knownDevices.txt', 'w')

try:
    file = open('namedDevices.txt', 'r')
except IOError:
    file = open('namedDevices.txt', 'w')

#scan for connected devices
while True:
	string="iw wlan1 station dump | grep Station"
	result=subprocess.getoutput(string)
	try:
		macAddr = result.split(" ")[1]
		with open('knownDevices.txt') as f:
			knownDevices = f.readlines()
			if macAddr not in knownDevices:
				with open("knownDevices.txt", "w") as file:
					file.write(macAddr + "\n")
	except:
		print("No devices connected yet")


	arpScan="sudo arp-scan --interface=wlan1 --localnet"
	allDevices=subprocess.getoutput(arpScan)
	listAllDevices = allDevices.splitlines()


	for element in listAllDevices:
		try:
			if macAddr in element:
				print ("Device connected: ", element)
				with open('namedDevices.txt') as f:
					namedDevices = f.readlines()
					if element not in namedDevices:
						with open("namedDevices.txt", "w") as file:
							file.write(element + "\n")

		except:
			pass



	time.sleep(10)
