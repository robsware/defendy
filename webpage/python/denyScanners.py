import os

ips = ["74.82.47.5",
"104.131.0.69",
"104.236.198.48",
"155.94.222.12",
"104.236.198.48",
"155.94.254.133",
"155.94.254.143",
"162.159.244.38",
"185.181.102.18",
"188.138.9.50",
"198.20.69.74",
"198.20.69.98",
"198.20.70.114",
"198.20.87.98",
"198.20.99.130",
"208.180.20.97",
"209.126.110.38",
"159.203.176.62",
"162.159.244.38",
"185.163.109.66",
"185.181.102.18",
"188.138.1.119",
"188.138.9.50",
"198.108.66.0/23",
"198.20.69.100",
"198.20.69.101",
"198.20.69.102",
"198.20.69.103",
"198.20.69.72",
"198.20.69.73",
"198.20.69.74",
"198.20.69.75",
"198.20.69.76",
"198.20.69.77",
"198.20.69.78",
"198.20.69.79",
"198.20.69.96",
"198.20.69.97",
"198.20.69.98",
"198.20.69.99",
"198.20.70.111",
"198.20.70.112",
"198.20.70.113",
"198.20.70.114",
"198.20.70.115",
"198.20.70.116",
"198.20.70.117",
"198.20.70.118",
"198.20.70.119",
"198.20.87.100",
"198.20.87.101",
"198.20.87.102",
"198.20.87.103",
"198.20.87.96",
"198.20.87.97",
"198.20.87.98",
"198.20.87.99",
"198.20.99.128",
"198.20.99.129",
"198.20.99.130",
"198.20.99.131",
"198.20.99.132",
"198.20.99.133",
"198.20.99.134",
"198.20.99.135",
"209.126.110.38",
"216.117.2.180",
"66.240.192.138",
"66.240.219.146",
"66.240.236.119",
"71.6.135.131",
"71.6.146.185",
"71.6.158.166",
"71.6.165.200",
"71.6.167.142",
"66.240.192.138",
"66.240.205.34",
"66.240.219.146",
"66.240.236.119",
"71.6.135.131",
"71.6.146.130",
"71.6.146.185",
"71.6.146.186",
"71.6.158.166",
"71.6.165.200",
"71.6.167.142",
"80.82.77.139",
"80.82.77.33",
"82.221.105.6",
"82.221.105.7",
"85.25.103.50",
"85.25.43.94",
"93.120.27.62",
"98.143.148.107",
"82.221.105.7",
"85.25.103.50",
"85.25.43.94",
"89.248.167.131",
"89.248.172.16",
"93.120.27.62",
"93.174.95.106",
"94.102.49.190",
"94.102.49.193",
"98.143.148.135"]

for ip in ips:
    os.system("iptables -A INPUT -j DROP -s " + ip)


#python /home/rob/defendy/webpage/python