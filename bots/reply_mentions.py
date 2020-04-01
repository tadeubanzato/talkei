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

api = tweepy.API(auth)

def check_mentions(api, keywords, since_id):
    print(bcolors.YELLOW + "Retrieving mentions...")

    for tweet in tweepy.Cursor(api.timeline).items():
        #new_since_id = max(tweet.id, new_since_id)

        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keywords in tweet.text.lower()):
            print(bcolors.BLUE + "Respondendo para: " + tweet.user.name)

            api.update_status(
                status="Esse presidente é um bossal, sem mais. #ForaBolsonaro #Bolsonazi #BolsonaroGenocida",
                in_reply_to_status_id=tweet.id,
            )
    return

def on_error(self, status):
    logger.error(status)

def main():
    # Create API connection
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "support"], since_id)
        logger.info("Will continue ine...")
        #time.sleep(60)
        t=(20)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(bcolors.RED + "Restart:" + bcolors.ENDC, timer, end="\r")
            time.sleep(1)
            t -= 1

if __name__ == "__main__":
    main()
