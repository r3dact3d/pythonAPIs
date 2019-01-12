#!/usr/bin/env python
# coded by brady [r3dact3d]
import requests
import json
from sys import argv

script, ip = argv
url = 'http://ip-api.com/json/' + ip
data = requests.get(url).json()
if data['status'] == 'fail':
    print '=================================='
    print '| Query failed for IP '+ data['query']
    exit()
print '================================'
print '| IP      ---> ' + data['query']
print '| ISP     ---> ' + data['isp']
print '| ORG     ---> ' + data['org']
print '| Region  ---> ' + data['regionName']
print '| Country ---> ' + data['country']
print '================================'
#print data['lat']
#print data['lon']
#print data['zip']
#print data['timezone']
#print data['contryCode'] 
