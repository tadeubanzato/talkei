#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/fav_retweet.py
import json
import tweepy
import time
import gspread
import random
import requests

"""
V1.03
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

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_error(self, status):
        logger.error(status)

    def on_status(self, tweet):

        # api = tweepy.API(auth, wait_on_rate_limit=True,
        #     wait_on_rate_limit_notify=True)

        print(bcolors.GREEN + "Processing tweet id: " + bcolors.ENDC, tweet.id)
        print(bcolors.BLUE + "Message: ", tweet.text, bcolors.ENDC)
        #lines = open('frases.txt').read().splitlines()
        #m =random.choice(lines)
        #m = random.choice(frases)
        #frases = ['Votou nesse energúmeno assina em baixo as mortes #Genocida #ForaBolsonaro #bolsoNazi', 'Não tem como defender os indefensável #Genocida #ForaBolsonaro #bolsoNazi', 'Impossível apoiar um genocida seja ele quem for #Genocida #ForaBolsonaro #bolsoNazi', 'Não vamos virar a Venezuela mas quem sabe a alemanha de 39 #Genocida #ForaBolsonaro #bolsoNazi', 'Incapaz, acéfalo, genocida, imvecí são os adjetivos para o Bolsonaro #Genocida #ForaBolsonaro #bolsoNazi','Ogado continua seguindo o líder #Genocidas #foraBolsonaro #AcabouBolsonaro']
        #m = random.choice(frases)
        m = 'Votou no Bolsonaro também assina os óbitos desse energúmeno #Bolsonazi #Genocida #ForaBolsonaro'  # our status message
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return

        else:
            print(bcolors.RED + "RESPONDENDO: ",m,bcolors.ENDC)
            #s = api.update_status(m)
            sn = tweet.user.screen_name
            #tweets = api.user_timeline(screen_name=user_name)
            m = "@%s %s" % (sn, m,)
            s = api.update_status(m, in_reply_to_status_id = tweet.id)

            #api.update_status('@{} Esse cara é uma piada #Genocida #ForaBolsonaro'.format(user_name), tweet.id)

    # except Exception as e:
    #     logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    try:
        api = tweepy.API(auth, wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True)
        tweets_listener = FavRetweetListener(api)
        stream = tweepy.Stream(api.auth, tweets_listener)
        stream.filter(track=keywords, languages=["pt"])
        reply_new_tweets()

    except tweepy.TweepError:
        t=(2)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(bcolors.RED + "Restart API back in:" + bcolors.ENDC, timer, end="\r")
            time.sleep(1)
            t -= 1

if __name__ == "__main__":
    main(["esquerdopata", "#BolsonaroTemRazao", "#EstadoDeDefesa", "esquerdopatia", "#ReajaPresidente", "O povo está com você", "Só orgulho Presidente"])
