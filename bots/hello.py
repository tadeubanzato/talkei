#!/usr/bin/env python3
# git pull origin master
import json
import tweepy
import logging
import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import random
from random import *

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('talkei-0c766b314509.json', scope)
client = gspread.authorize(creds)

# sheet = client.open('Talkei_Messages').sheet1
# talkeiMessage = sheet.get_all_records()
# print(talkeiMessage)

#max_rows = len(worksheet.get_all_values())
#this is a list of list of all data and the length is equal to the number of rows including header row if it exists in data set
x = randint(1, 100)
print (x)

sheet = client.open('Talkei_Messages').sheet1
pp = pprint.PrettyPrinter()

fillrows = len(sheet.get_all_values()) # Get total number of rolls with data added
#talkeiMessage = sheet.cell(3, 1).value
randNumber = (random.randrange(fillrows))
print ("Total rows: " + randNumber)
x = randint(1, randNumber)

talkeiMessage = sheet.cell(x,1).value
print(talkeiMessage)



# #to get all the values inside the file
# sheet.get_all_values()
# #to get exact row values in a second row (Since 1st row is the header)
# sheet.row_values(2)
# #to get all the column values in the column 'place'
# sheet.col_values(16)
# #to extract a particular cell value
# sheet.cell(1, 1).value
# pp.pprint(talkeiMessage)

# logger = logging.getLogger()
#
# # Authenticate to Twitter
# auth = tweepy.OAuthHandler("i0fnpu89sMI8QMnyGKHJkdyYS",
#     "ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv")
# auth.set_access_token("1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk",
#     "9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i")
#
# # Create API object
# api = tweepy.API(auth, wait_on_rate_limit=True,
#     wait_on_rate_limit_notify=True)
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()
#
# api.update_status("Hello Tweepy")
