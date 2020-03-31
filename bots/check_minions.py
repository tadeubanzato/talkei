#!/usr/bin/env python3
import os

"""
Check to see if an process is running. If not, restart.
Run this in a cron job
"""
import os
process_name= "minion2.py" # change this to the name of your process

tmp = os.popen("ps -Af").read()

if process_name not in tmp[:]:
    print "The process is not running. Let's restart."
    """"Use nohup to make sure it runs like a daemon"""
    newprocess="nohup python3 %s &" % (process_name)
    os.system(newprocess)
else:
    print "The process is running."
