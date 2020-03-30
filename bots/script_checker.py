#!/usr/bin/env python3
import psutil
import sys
from subprocess import Popen

for process in psutil.process_iter():
    if process.cmdline() == ['python3', 'minions_reply_OLD.py']:
        print("Minions Bot working")
        if process.cmdline() == ['python3', 'fav_retweet.py']:
            print("Fav and Retweet bot working")
        elif print('Process not found: starting it.')
            Popen(['python3', 'fav_retweet.py'])
    elif print("Starting Minions")
        Popen(Popen(['python3', 'minions_reply_OLD.py']))

    sys.exit('Good Job!')
