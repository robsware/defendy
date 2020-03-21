import os
import iptc

import requests
publicIP = requests.get('http://ifconfig.me')

publicIP = publicIP.content
publicIP = publicIP.decode("utf-8") 


with open("publicIP.txt", "w") as f:
    f.writelines(publicIP)