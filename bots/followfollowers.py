#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/followfollowers.py

import json
import tweepy
import logging
import os
import time

logger = logging.getLogger()

# Authenticate to Twitter
auth = tweepy.OAuthHandler("i0fnpu89sMI8QMnyGKHJkdyYS",
    "ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv")
auth.set_access_token("1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk",
    "9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# def limit_handled(cursor):
#     while True:
#         try:
#             yield cursor.next()
#         except tweepy.RateLimitError:
#             time.sleep(15 * 60)
#
# for follower in limit_handled(tweepy.Cursor(api.followers).items()):
#     if follower.friends_count < 50:
#         print(follower.screen_name)
#
#
# users = tweepy.Cursor(api.followers, screen_name=accountvar).items()
#
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    print "@" + user.screen_name


# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()
#
# # FOLLOW FOLLOWERS
# def follow_followers(api):
#     print("Retrieving and following followers")
#     for follower in tweepy.Cursor(api.followers).items():
#         if not follower.following:
#             print("Following: " + follower.name)
#             follower.follow()
#
# def main():
#     #api = create_api()
#     while True:
#         follow_followers(api)
#         print("Waiting...")
#         time.sleep(60)
#
# if __name__ == "__main__":
#     main()
