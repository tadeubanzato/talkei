#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# git pull origin master

import json
import tweepy
import logging
import os
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("i0fnpu89sMI8QMnyGKHJkdyYS",
    "ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv")
auth.set_access_token("1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk",
    "9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
print("TESTE")
# STREAM TIMELINE TWEETS amd RETWEETS
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print (tweet.user.name + " said: " + tweet.text)

        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return

        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                #logger.exception("Error on fav", exc_info=True)
                time.sleep(30)
                #return

        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                print ("\n\n Retweeted \n\n")
                if not tweet.user.following:
                    tweet.user.follow()
                    time.sleep(15 * 30)
                    return

            except Exception as e:
                logger.error("Error on fav and retweet") #, exc_info=True
                time.sleep(50)
                return
                # In this example, the handler is time.sleep(15 * 60),

            # but you can of course handle it in any way you want.

        def limit_handled(cursor):
            while True:
                try:
                    yield cursor.next()
                except tweepy.RateLimitError:
                    time.sleep(15 * 60)

             #for follower in limit_handled(tweepy.Cursor(api.followers).items()):
                #if follower.friends_count < 300:
                    #print(follower.screen_name)

                def on_error(self, status):
                    print("Error detected")


tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Bolsonazi", "biroliro", "bolsonaro imbecil", "#BolsonaroGenocida", "#Bolsonaroacabou", "#ForaBolsonaro", "#BolsonaroNaoEmaisPresidente"], languages=["pt"])
