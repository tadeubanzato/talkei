#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/fav_retweet.py

import tweepy
import logging
import json
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("i0fnpu89sMI8QMnyGKHJkdyYS",
    "ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv")
auth.set_access_token("1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk",
    "9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Create API object
# api = tweepy.API(auth, wait_on_rate_limit=True,
#     wait_on_rate_limit_notify=True)

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
        print(bcolors.WARNING + "Processing tweet id: " + bcolors.ENDC, tweet.id)
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited or tweepy.TweepError:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)

            except tweepy.TweepError:
                t=(60 * 15)
                while t:
                    mins, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(bcolors.FAIL + "API rest on error 1, restarting in:" + bcolors.ENDC, timer, end="\r")
                    time.sleep(1)
                    t -= 1

        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                if not tweet.user.following:
                    print(bcolors.HEADER + "Following user: " + bcolors.ENDC,tweet.user.name)
                    #time.sleep(60 * 15)
                    t=(60 * 15)
                    while t:
                        mins, secs = divmod(t, 60)
                        timer = '{:02d}:{:02d}'.format(mins, secs)
                        print(bcolors.FAIL + "API rest on follow, restarting in:" + bcolors.ENDC, timer, end="\r")
                        time.sleep(1)
                        t -= 1

            except tweepy.TweepError:
                t=(60 * 15)
                while t:
                    mins, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(bcolors.FAIL + "API rest on error 2, restarting in:" + bcolors.ENDC, timer, end="\r")
                    time.sleep(1)
                    t -= 1

            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    #api = create_api()
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["pt"])

if __name__ == "__main__":
    main(["#ForaBolsonaro", "#BolsonaroGenocida", "#BolsoNazi", "#Bolsonaroacabou", "#BolsonaroNaoEmaisPresidente", "biroliro", "bolsonaro imbecil"])
