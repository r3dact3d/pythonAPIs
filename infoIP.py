#!/usr/bin/env python3
# coded by brady [r3dact3d]
import requests
import json
from sys import argv

def hitAPI(ip):
    url = 'http://ip-api.com/json/' + ip
    data = requests.get(url).json()
#    print(data)
    if data['status'] == 'fail':
        print('| Query failed for IP '+ data['query'])
        exit()
    else:
    	print('================================')
    	print('| IP      ---> ' + data['query'])
    	print('| ISP     ---> ' + data['isp'])
    	print('| ORG     ---> ' + data['org'])
    	print('| Region  ---> ' + data['regionName'])
    	print('| Country ---> ' + data['country'])
    	print('================================')
    	exit()

if len(argv) < 2:
    print('Usage: ./infoIP.py "Put IP address to lookup here"')
    exit()
else:
    script, ip = argv 
    hitAPI(ip)

