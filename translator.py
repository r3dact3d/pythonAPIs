#!/usr/bin/env python
# writtent by brady [r3dact3d]
# Include what you want to translate after calling script
import requests
import json
from sys import argv
text = ''
argv.pop(0)
for i in argv:
    text = text +" " + i
params = { 'text' : text }
langList = 'ermahgerd brooklyn uk2us us2uk morse cockney fudd dolan jive vulcan shakespeare oldenglish chef huttese mandalorian gungan cheunh sith quenya sindarin valyrian dothraki piglatin ferblatin minion valspeak pirate yoda'
print langList
lang = raw_input('Pick language: ')
if lang not in langList:
     print 'You didn\'t pick a language from the list!'
     exit()
url = 'http://api.funtranslations.com/translate/' + lang + '.json'
page = requests.get(url, params=params)
#print page.url
j = page.json()
print "#######################################################"
print j['contents']['translated']
