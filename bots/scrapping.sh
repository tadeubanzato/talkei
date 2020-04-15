#!/bin/sh

CHECK='ps aux | grep minions_scrapping2.py | grep -v grep | wc -l'

if [ $CHECK = 0 ]
then
	python3 /home/pi/talkei/bots/minions_scrapping2.py &
else

fi
