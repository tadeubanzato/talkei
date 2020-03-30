import psutil
import sys
from subprocess import Popen

for process in psutil.process_iter():
    if process.cmdline() == ['python3', 'minions_reply_OLD.py']:
        print('Minions Runing Well')
    else print ("Restarting Minions")
        Popen(['python3', 'your_script.py'])ls

    if process.cmdline() == ['python3', 'fav_retweet.py']:
        print('FAV Runing Well')
    else print("Restarting FAV")
        Popen(['python3', 'fav_retweet.py'])ls

sys.exit('Good Job!')
