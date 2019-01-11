#!/usr/bin/env python
# writtent by brady [r3dact3d]
# Include what you want to translate after calling script
import requests
import json
from sys import argv

text = ''
langList = '''
ermahgerd brooklyn uk2us us2uk morse cockney fudd dolan jive vulcan shakespeare oldenglish 
chef huttese mandalorian gungan cheunh sith quenya sindarin valyrian dothraki piglatin 
ferblatin minion valspeak pirate yoda numbers emoji
'''
def hitAPI(langList, params):
    print(langList)
    lang = raw_input('Ping language: ')
    if lang not in langList:
        print('You didn\'t pick a language from the list!')
        exit()
    url = 'http://api.funtranslations.com/translate/' + lang + '.json'
    page = requests.get(url, params=params)
    if page.status_code == 200:
        j = page.json()
        print "#######################################################"
        print(j['contents']['translated'])
        exit()
    else:
        print('Something went wrong with the API, probably exceeded rate limit for this hour!')
        exit()

if len(argv) < 2:
    print('Usage: ./translator.py "Put text to translate here"')
    exit()
else:
    argv.pop(0)
    for i in argv:
        text = text +" " + i
    params = {'text' : text}     
    hitAPI(langList, params)
