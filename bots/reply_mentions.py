#!/usr/bin/env python3
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

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(format=logging.INFO)
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
            logger.info("Answering" + tweet.user.name)

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status="Please reach us via DM",
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def main():
    #api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "support"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()

# tweets_listener = MyStreamListener(api)
# stream = tweepy.Stream(api.auth, tweets_listener)
# stream.filter(track=["Bolsonazi", "biroliro", "bolsonaro imbecil", "#BolsonaroGenocida", "#Bolsonaroacabou", "#ForaBolsonaro", "#BolsonaroNaoEmaisPresidente"], languages=["pt"])


# # FOLLOW FOLLOWERS
# def follow_followers(api):
#     logger.info("Retrieving and following followers")
#     for follower in tweepy.Cursor(api.followers).items():
#         if not follower.following:
#             logger.info("Following: " + follower.name)
#             follower.follow()
#
# def main():
#     #api = create_api()
#     while True:
#         follow_followers(api)
#         logger.info("Waiting...")
#         time.sleep(60)
#
# if __name__ == "__main__":
#     main()

# Likes all tweet mentions
# tweets = api.mentions_timeline()
# for tweet in tweets:
#     tweet.favorite()
#     tweet.user.follow()
#
# for tweet in tweepy.Cursor(api.home_timeline).items(100):
#     print(tweet.user.name + " said: " + tweet.text
#
# def on_status(self, status):
#     if hasattr(status, "retweeted_status"):  # Check if Retweet
#         try:
#             print(status.retweeted_status.extended_tweet["full_text"])
#         except AttributeError:
#             print(status.retweeted_status.text)
#     else:
#         try:
#             print(status.extended_tweet["full_text"])
#         except AttributeError:
#             print(status.text)

# # Method search
# for tweet in api.search(q="bolsonazi", lang="pt", rpp=10):
#     #print(f"{tweet.user.name}:{tweet.text}")
#     print (tweet.user.name + ':' + tweet.text)
#     tweet.favorite()
#     def on_status(self, status):
#
#     for follower in tweepy.Cursor(api.followers).items():
#         if not follower.following:
#             logger.info("Following " + follower.name)
#             follower.follow()
#             api.create_friendship(tweet.user.name)
#
#     #tweet.favorite()
#
#
# class MyStreamListener(tweepy.StreamListener):
#     def __init__(self, api):
#         self.api = api
#         self.me = api.me()
#
#     def on_status(self, tweet):
#         print(tweet.user.name + ' : ' + tweet.text)
#
#     def on_error(self, status):
#         print("Error detected")
#
# tweets_listener = MyStreamListener(api)
# stream = tweepy.Stream(api.auth, tweets_listener)
# stream.filter(track=["Bolsonazi"], languages=["pt"])
# time.sleep(60)

# # Method Liking
# tweets = api.home_timeline(count=1)
# tweet = tweets[0]
# #print tweet.id
# #print tweet.author.name
# print('Liking tweet' + tweet.id + ' of ' + tweet.author.name)
# api.create_favorite(tweet.id)


# class FavRetweetListener(tweepy.StreamListener):
#     def __init__(self, api):
#         self.api = api
#         self.me = api.me()
#
#     def on_status(self, tweet):
#         logger.info("Processing tweet id: " + tweet.id)
#         if tweet.in_reply_to_status_id is not None or \
#             tweet.user.id == self.me.id:
#             # This tweet is a reply or I'm its author so, ignore it
#             return
#         if not tweet.favorited:
#             # Mark it as Liked, since we have not done it yet
#             try:
#                 tweet.favorite()
#             except Exception as e:
#                 logger.error("Error on fav", exc_info=True)
#         if not tweet.retweeted:
#             # Retweet, since we have not retweeted it yet
#             try:
#                 tweet.retweet()
#             except Exception as e:
#                 logger.error("Error on fav and retweet", exc_info=True)
#
#     def on_error(self, status):
#         logger.error(status)
#
# def main(keywords):
#     #api = create_api()
#     tweets_listener = FavRetweetListener(api)
#     stream = tweepy.Stream(api.auth, tweets_listener)
#     stream.filter(track=keywords, languages=["pt"])
#
# if __name__ == "__main__":
#     #main(["Bolsonazi", "Tweepy"])
#     main(["Bolsonazi"])
