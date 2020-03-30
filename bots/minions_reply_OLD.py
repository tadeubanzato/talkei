#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/fav_retweet.py
import json
import tweepy
import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
from random import *
import requests

"""
V1.03
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

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/talkei/bots/talkei-0c766b314509.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Talkei_Messages').sheet2

fillrows = len(sheet.get_all_values()) # Get total number of rolls with data added
x = randint(1, fillrows)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_error(self, status):
        logger.error(status)

    def on_status(self, tweet):

        # api = tweepy.API(auth, wait_on_rate_limit=True,
        #     wait_on_rate_limit_notify=True)

        print(bcolors.GREEN + "Processing tweet id: " + bcolors.ENDC, tweet.id)
        print(bcolors.BLUE + "Message: ", tweet.text, bcolors.ENDC)
        m = sheet.cell(x,1).value
        #m = 'Votou no Bolsonaro também assina os óbitos desse energúmeno #Bolsonazi #Genocida #ForaBolsonaro'  # our status message
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return

        else:
            print(bcolors.RED + "RESPONDENDO: ",m,bcolors.ENDC)
            #s = api.update_status(m)
            sn = tweet.user.screen_name
            #tweets = api.user_timeline(screen_name=user_name)
            m = "@%s %s" % (sn, m,)
            s = api.update_status(m, in_reply_to_status_id = tweet.id)

            #api.update_status('@{} Esse cara é uma piada #Genocida #ForaBolsonaro'.format(user_name), tweet.id)

    # except Exception as e:
    #     logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    try:
        tweets_listener = FavRetweetListener(api)
        stream = tweepy.Stream(api.auth, tweets_listener)
        stream.filter(track=keywords, languages=["pt"])
        reply_new_tweets()

    except tweepy.TweepError:
        t=(60 * 15)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(bcolors.RED + "Restart API back in:" + bcolors.ENDC, timer, end="\r")
            time.sleep(1)
            t -= 1

if __name__ == "__main__":
    main(["esquerdopata", "#BolsonaroTemRazao", "#EstadoDeDefesa", "esquerdopatia", "#ReajaPresidente", "O povo está com você", "Só orgulho Presidente"])
