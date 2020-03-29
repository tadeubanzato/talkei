#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/followfollowers.py
import json
import tweepy
import logging
import os
import time

# Create color code
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

# FOLLOW FOLLOWERS
def follow_followers(api):
    print("Retrieving and following followers")
    print(bcolors.BLUE + "Retrieving and following followers" + bcolors.ENDC)
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            print(bcolors.GREEN + "Following: " + bcolors.ENDC,follower.name)
            follower.follow()

def main():
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    #api = create_api()
    while True:
        follow_followers(api)
        print("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
