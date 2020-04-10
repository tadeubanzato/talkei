#!/usr/bin/en python3
# -*- coding: utf-8 -*-
# bots/ping_runing.py
import requests
import sys

## IFTTT and Webhook alet
# Array for the values on Webhook ["value1"], ["value2"], etc
report = {}

# Webhook will receive IP address from the pi
report["value1"] = "Starting script: "

# Get DashPi IP address
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
#s.close()
print (sys.argv[1])
runing = str(sys.argv[1])
report["value2"] = runing

# Resquest post to Webhook integrated with IFTTT
requests.post('https://maker.ifttt.com/trigger/Talkei/with/key/d1oS5w-uq90y8fCs2ot5qG', data=report)