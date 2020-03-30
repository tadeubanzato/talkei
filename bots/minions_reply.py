#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/fav_retweet.py
import tweepy
import cPickle
import logging
import json
import time

"""
This script is for listening Twitter timeline and:
1. Favorsite all twits with the comments based on the search keywords
2. Retweet any twits with the search keywords criteria
3. Follow any users with that twitted with the search criteria

V1.02
"""

# Create color code
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#-------------------------------------------------------------------------------
def login():
    ''' Takes our credentials and logs into Twitter using OAuth. A Tweepy
        api object is returned upon success. '''
    consumer_token = credentials['i0fnpu89sMI8QMnyGKHJkdyYS']
    consumer_secret = credentials['ruWDxELm9PSAwnbrz6PcxZ7TFaPfQqPeoLn7g2rYuN2PsRisyv']
    access_token = credentials['1106313860460568576-wVk6Olx2T3dmwMB8A4iDGC7jmzWkhk']
    access_token_secret = credentials['9iGV5ruDnAw4bcTxf5Slpwu9NqvsugDSqJtHJXGJNTK4i']

    api = None
    try:
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except tweepy.TweepError, e:
        print e
    return api


#-------------------------------------------------------------------------------
def shipit(api=None, replytostatus=None):
    ''' Tweets a status update. '''
    if api is None:
        api = login()
    m = 'Esse cara é um loco isso sim #Genocida #ForaBolsonaro'  # our status message
    try:
        if replytostatus is None:
            s = api.update_status(m)
        else:
            # If replying, do some extra formatting of the status message.
            sn = replytostatus.user.screen_name
            m = "@%s %s" % (sn, m,)
            s = api.update_status(m, replytostatus.id)
    except tweepy.TweepError, e:
        print e

#-------------------------------------------------------------------------------
def main():
    try:
        listened = cPickle.load(open('listened.pkl','r'))
    except:
        listened = []

    # We're going to loop indefinitely, pausing between checks.
    while True:
        api = update_following()
        listen_to_friends(api, listened)
        cPickle.dump(listened,open('listened.pkl', 'w'))
        print time.ctime()
        time.sleep(60)

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# if __name__ == "__main__":
#     main(["esquerdopata", "#BolsonaroTemRazao", "#EstadoDeDefesa", "esquerdopatia", "#ReajaPresidente", "O povo está com você", "Só orgulho Presidente"])
