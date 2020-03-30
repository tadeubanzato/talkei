#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/fav_retweet.py
import tweepy
import logging
import json
import time

"""
This script is for replying to any mentions on Twitter timeline and:

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

def check_mentions(api, keywords, since_id):
    print(bcolors.YELLOW + "Retrieving mentions...")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            print(bcolors.BLUE + "Respondendo para: " + tweet.user.name)

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status="Esse presidente é um bossal, sem mais. #ForaBolsonaro #Bolsonazi #BolsonaroGenocida",
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def on_error(self, status):
    logger.error(status)

def main():

    while True:
        since_id = check_mentions(api, ["help", "support"], since_id)
        logger.info("Will continue ine...")
        #time.sleep(60)
        t=(60)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(bcolors.RED + "Restart:" + bcolors.ENDC, timer, end="\r")
            time.sleep(1)
            t -= 1

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