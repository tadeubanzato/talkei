#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/fav_retweet.py
import tweepy
import logging
import json
import time
import os
from pandas import DataFrame

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

class TweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_error(self, status):
        logger.error(status)

    def on_status(self, tweet):
        print(bcolors.GREEN + "Tweet from: " + bcolors.ENDC, tweet.user.name)
        print(bcolors.BLUE + "Message: ", tweet.text, bcolors.ENDC,"\n")
        check = tweet.text[:2]
        pint(check)
        # if check[:2] is not "RT"
        #     flagNew = "NEW TWEET"
        #     return

        minions =({'Tweet ID':[tweet.id],'User Name':[tweet.user.screen_name],'User URL':['https://twitter.com/'+tweet.user.screen_name],'Friend Counts':[tweet.user.friends_count],'Followers':[tweet.user.followers_count],'Created':[tweet.user.created_at],'Location':[tweet.user.location],'Tweet':[tweet.text],'Tweet Link':['https://twitter.com/'+tweet.user.screen_name+'/status/'+tweet.id], 'New Tweet':flagNew})
        df = DataFrame(minions)
        df.to_csv ('/home/pi/talkei/minions_log.csv', columns=['Tweet ID', 'User Name', 'User URL', 'Friend Counts', 'Followers', 'Created', 'Location','Tweet','Tweet Link','New Tweet'], encoding='utf-8', index=False, header=None, mode='a') # here you have to write path, where result file will be stored

        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it porque vc nao ta atualizando?
            return

        # check = tweet.text
        # if check[:2] is not 'RT' or tweet.in_reply_to_status_id is not None
        #     #print(check[:2])

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
