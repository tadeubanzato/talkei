# tweepy-bots/bots/favretweet.py

import tweepy
import logging
import json
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("i0fnpu89sMI8QMnyGKHJkdyYS",
    "ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv")
auth.set_access_token("1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk",
    "9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# Create LOGGER object
logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    # # # LIMIT HANDLER STARTS HERE
    # def limit_handled(cursor):
    #     print("limit handler")
    #     while True:
    #         try:
    #             yield cursor.next()
    #         except tweepy.RateLimitError:
    #             print("start handler")
    #             time.sleep(15 * 60)

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_error(self, status):
        logger.error(status)

    def on_status(self, tweet):
        print("Processing tweet id ", tweet.id)

        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)

        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                #tweet.user.follow()
                print("Following user: ",tweet.user)

            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    #api = create_api()
    time.sleep(100)
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["pt"])

if __name__ == "__main__":
    main(["#ForaBolsonaro", "#BolsonaroGenocida", "#BolsoNazi"])
    time.sleep(15)
#all tags
#"Bolsonazi", "biroliro", "bolsonaro imbecil", "#BolsonaroGenocida", "#Bolsonaroacabou", "#ForaBolsonaro", "#BolsonaroNaoEmaisPresidente"


# c = tweepy.Cursor(api.search,
#                        q=search,
#                        include_entities=True).items()
# while True:
#     try:
#         tweet = c.next()
#         # Insert into db
#     except tweepy.TweepError:
#         time.sleep(60 * 15)
#         continue
#     except StopIteration:
#         break
