#with open('/var/log/suricata/fast.log') as f:
with open('webpage/fast.log') as f:
    alerts = f.readlines()
    for line in alerts:
        if '[Priority: 1]' in line or '[Priority: 2]' in line:
            line = line.split('{TCP} ')[1]
            line = line.split(' ')[0]
            print (line)

