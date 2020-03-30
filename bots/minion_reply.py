#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/fav_retweet.py
import tweepy
import logging
import json
import time

"""
This script is for listening Twitter timeline and:
1. Favorsite all twits with the comments based on the search keywords
2. Retweet any twits with the search keywords criteria
3. Follow any users with that twitted with the search criteria

V1.02
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

# Create LOGGER object
logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_error(self, status):
        logger.error(status)

    def on_status(self, tweet):
        print(bcolors.GREEN + "Processing tweet id: " + bcolors.ENDC, tweet.id)
        print(bcolors.BLUE + "Message: ", tweet.text, bcolors.ENDC)
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if any(keywords in tweet.text.lower() for keywords in keywords):
            print(bcolors.BLUE + "Respondendo para: " + tweet.user.name)
            api.update_status(
                status="Esse presidente é um bossal, isso sim! Você também tem culpa. #ForaBolsonaro #Bolsonazi #BolsonaroGenocida",
                in_reply_to_status_id=tweet.id,
            )
        return

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    try:
        # Create API connection
        api = tweepy.API(auth, wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True)
        tweets_listener = FavRetweetListener(api)
        stream = tweepy.Stream(api.auth, tweets_listener)
        stream.filter(track=keywords, languages=["pt"])

    except tweepy.TweepError:
        t=(60 * 15)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(bcolors.RED + "Restart API back in:" + bcolors.ENDC, timer, "\r")
            time.sleep(1)
            t -= 1

if __name__ == "__main__":
    main(["esquerdopata", "esquerdopatia", "#BolsonaroTemRazao", "O POVO É BOLSONARO", "Estamos juntos Presidente", "Só orgulho Presidente", "#ReajaPresidente"])