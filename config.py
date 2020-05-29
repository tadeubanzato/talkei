import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("i0fnpu89sMI8QMnyGKHJkdyYS")
    consumer_secret = os.getenv("ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv")
    access_token = os.getenv("1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk")
    access_token_secret = os.getenv("9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
