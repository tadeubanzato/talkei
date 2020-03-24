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

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('talkei-0c766b314509.json', scope)
client = gspread.authorize(creds)

# sheet = client.open('Talkei_Messages').sheet1
# talkeiMessage = sheet.get_all_records()
# print(talkeiMessage)

sheet = client.open('Talkei_Messages').sheet1
pp = pprint.PrettyPrinter()
employees = sheet.get_all_records()
pp.pprint(employees)

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
