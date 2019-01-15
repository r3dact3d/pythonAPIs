#!/usr/bin/env python
# written by brady [r3dact3d]
import requests

url = 'http://api.open-notify.org/astros.json'
j = requests.get(url).json()
number = j['number']
people = j['people']

print "=================================="
print "Humans in space currently: %s" % number
for i in range(0, number):
    boat = j['people'][i]['craft']
    name = j['people'][i]['name']
    print "Craft: %s             Name: %s" % (boat, name)
    print "---------------------------------------"
