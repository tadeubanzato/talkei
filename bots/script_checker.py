import psutil
import sys
from subprocess import Popen

for process in psutil.process_iter():
    if process.cmdline() == ['python3', 'fav_retweet.py ']:
        sys.exit('Process found: exiting.')

print('Process not found: starting it.')
Popen(['python3', 'fav_retweet.py'])
