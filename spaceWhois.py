#!/usr/bin/env python
import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url).text
print(f"""
Provide information regarding :param people:he details below concerning astronauts, humans, and people in space. 
Provide summary and interesting information regarding the craft the person is on.
Report the number as the number of people in space.
{response}
""")
#response = requests.get(url).json()
#number = response["number"]
#people = response["people"]
#return = f"There are {number} people in space."
#print("==================================")
#print(f"Humans in space currently: {number}")
#for i in range(0, number):
#    boat = people[i]["craft"]
#    name = people[i]["name"]
#    print(f"Craft: {boat}             Name: {name}")
#    print("---------------------------------------")
