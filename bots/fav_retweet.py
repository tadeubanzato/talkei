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
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_error(self, status):
        logger.error(status)

    def on_status(self, tweet):
        time.sleep(30)
        print("Processing tweet id ", tweet.id)

        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited or tweepy.TweepError:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                time.sleep(30)
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
            except tweepy.TweepError:
                time.sleep(60 * 15)
                item = next(items)

        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                if not tweet.user.following:
                    while True:
                        try:
                            item = next(items)
                        except tweepy.TweepError:
                            time.sleep(60 * 15)
                            item = next(items)
                        print item
                # if not tweet.user.following:
                #     tweet.user.follow()
                #     time.sleep(5 * 60)
                #     return
                    # print("Following: ",tweet.user)
                    # print(")
                    # time.sleep(15 * 30)
            except tweepy.TweepError:
                time.sleep(60 * 15)
                item = next(items)
                
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    #api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["pt"])

if __name__ == "__main__":
    main(["#ForaBolsonaro", "#BolsonaroGenocida", "#BolsoNazi", "#Bolsonaroacabou", "#BolsonaroNaoEmaisPresidente", "biroliro", "bolsonaro imbecil"])
