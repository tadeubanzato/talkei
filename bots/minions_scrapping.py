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

        minions =({'Tweet ID':[tweet.id],'User Name':[tweet.user.screen_name],'User URL':[tweet.user.url],'Friend Counts':[tweet.user.friends_count],'Followers':[tweet.user.followers_count]})
        #,tweet.user.time_zone,tweet.user.created_at,tweet.user.location,tweet.text]
        df = DataFrame(minions)
        df.to_csv ('/home/pi/talkei/minions_log.csv', index=False, header=True) # here you have to write path, where result file will be stored


# from pandas import DataFrame
# C = {['Python','Java', 'C++'],
#         'Designed by': ['Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup'],
#         'Appeared': ['1991', '1995', '1985'],
#         'Extension': ['.py', '.java', '.cpp'],
#     }
# df = DataFrame(C, columns= ['Programming language', 'Designed by', 'Appeared', 'Extension'])
# export_csv = df.to_csv (r'X:\pandaresult.csv', index = None, header=True) # here you have to write path, where result file will be stored
# print (df)



        # # Write a new roll with the information on the CSV file
        # with open('/home/pi/talkei/minions_log.csv', mode='w') as csv_file:
        #     fieldnames=['Tweet ID', 'User Name','User URL','Friends Count','Followers Count','Timezone', 'Created at', 'Location', 'Tweet']
        #     minions=csv.DictWriter(csv_file, fieldnames=fieldnames)
        #
        #     minions.writeheader()
        #     minions.writerows({'Tweet ID':tweet.id, 'User Name':tweet.user.screen_name, 'User URL':tweet.user.url, 'Friends Count':tweet.user.friends_count, 'Followers Count':tweet.user.followers_count, 'Timezone':tweet.user.time_zone, 'Created at':tweet.user.created_at, 'Location':tweet.user.location, 'Tweet':tweet.text})


        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it porque vc nao ta atualizando?
            return

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
