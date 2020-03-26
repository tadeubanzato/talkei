#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/hello.py

import json
import tweepy
import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
from random import *
import requests

# Create color code
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Authenticate to Twitter
auth = tweepy.OAuthHandler("i0fnpu89sMI8QMnyGKHJkdyYS",
    "ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv")
auth.set_access_token("1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk",
    "9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('talkei-0c766b314509.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Talkei_Messages').sheet1

fillrows = len(sheet.get_all_values()) # Get total number of rolls with data added
x = randint(1, fillrows)

talkeiMessage = sheet.cell(x,1).value
print(bcolors.GREEN + "Message that will be twitted: " + bcolors.ENDC, )
t = (10)
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Enviando!!!')
api.update_status(talkeiMessage)

# Webhook will send the tweet message to IFTTT
report = {}
report["value1"] = (sheet.cell(x,1).value)
requests.post('https://maker.ifttt.com/trigger/Talkei/with/key/d1oS5w-uq90y8fCs2ot5qG', data=report)


## Examples of code to get data from Google Sheets
# #to get all the values inside the file
# sheet.get_all_values()
# #to get exact row values in a second row (Since 1st row is the header)
# sheet.row_values(2)
# #to get all the column values in the column 'place'
# sheet.col_values(16)
# #to extract a particular cell value
# sheet.cell(1, 1).value
# pp.pprint(talkeiMessage)
