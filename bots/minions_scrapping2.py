#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/fav_retweet.py
import json
import tweepy
import logging
import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
from random import *
import requests

"""
This script scrapes twitter data and store key information of the users based on the criterias.
In thi case, the script search for keywords, identify users, use pandas to create a data structure
and save user information in a CSV file.

V1.1
"""

# Authenticate to Twitter
auth = tweepy.OAuthHandler("i0fnpu89sMI8QMnyGKHJkdyYS",
    "ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv")
auth.set_access_token("1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk",
    "9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i")

# Create color code
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Connecting to Google Sheets
print(bcolors.BLUE + "Connecting to Google Sheet" + bcolors.ENDC)
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/talkei/bots/talkei-0c766b314509.json', scope)
client = gspread.authorize(creds)
sheet = client.open('MinionsCount').sheet1 # discover total rows on sheet
index = len(sheet.get_all_values())


# Create LOGGER object
logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger()

class TweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_error(self, status):
        logger.error(status)

    def on_status(self, tweet):
        print(bcolors.GREEN + "Tweet from: " + bcolors.ENDC, tweet.user.name)
        print(bcolors.BLUE + "Message: ", tweet.text, bcolors.ENDC)
        twtLink =  'https://twitter.com/' + tweet.user.screen_name + '/status/' + str(tweet.id)
        print(twtLink,"\n")
        print(tweet.coordinates)

        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it porque vc nao ta atualizando?
            return

        # Flag if new tweet or RT
        check = tweet.text
        if check[:2] == "RT":
            flagNew = "RT"
        else:
            flagNew = "NEW TWEET"

        print(bcolors.RED + "Writing data to Sheets" + bcolors.ENDC)
        # Write data on Google Sheets
        row = [tweet.user.screen_name,tweet.user.friends_count,tweet.user.followers_count,tweet.user.created_at,tweet.user.location,flagNew,'https://twitter.com/' + tweet.user.screen_name,twtLink]
        index = index + 1
        sheet.insert_row(row, index)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    try:
        # Create API connection
        api = tweepy.API(auth, wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True)
        tweets_listener = TweetListener(api)
        stream = tweepy.Stream(api.auth, tweets_listener)
        stream.filter(track=keywords, languages=["pt"])

    except tweepy.TweepError:
        t=(60 * 15)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(bcolors.RED + "Restart API back in:" + bcolors.ENDC, timer, end="\r")
            time.sleep(1)
            t -= 1

if __name__ == "__main__":
    # Define keywords comma separated
    main(["#BolsonaroTemRazao", "esquerdopato", "#EstadoDeDefesa", "#ReajaPresidente", "presidente estamos com você", "força presidente", "seja forte bolsonaro", "Você não está sozinho capitão"])
