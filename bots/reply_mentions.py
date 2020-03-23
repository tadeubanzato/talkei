#!/usr/bin/env python
# bots/reply_mentions.py

import tweepy
import logging
from config import create_api
import time
import os

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

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info("Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status="Please reach us via DM",
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "support"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
