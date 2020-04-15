#!/bin/sh

CHECK='ps -aux | minions_scrapping2.py  | grep -v grep | wc -l'

if $CHECK -eq 0
  then
  	python3 /home/pi/talkei/bots/minions_scrapping2.py &

fi
