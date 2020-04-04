#!/usr/bin/python
with open('/var/log/suricata/fast.log') as f:
#with open('fast.log') as f:
	alerts = f.readlines()
	with open ('fast_prio.log', 'w') as wf:
		for line in alerts:
			if '[Priority: 1]' in line or '[Priority: 2]' in line:
				#line = line.split('{TCP} ')[1]
				#line = line.split(' ')[0]
				wf.write(line)
				print (line)

