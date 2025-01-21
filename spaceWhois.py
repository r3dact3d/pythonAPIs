#!/usr/bin/env python
import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url).json()
number = response["number"]
people = response["people"]
output = f"There are {number} people in space."
print("==================================")
print(f"Humans in space currently: {number}")
for i in range(0, number):
    boat = people[i]["craft"]
    name = people[i]["name"]
    print(f"Craft: {boat}             Name: {name}")
    print("---------------------------------------")
