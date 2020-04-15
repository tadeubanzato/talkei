#!/bin/sh

var1=`ps aux | grep minions_scrapping2.py | grep -v grep | wc -l`
echo $var1
if [ $var1 -eq 1 ]
then
  echo "The Process is Running"
else
  echo "Starting process"
  python3 /home/pi/talkei/bots/minions_scrapping2.py &
fi
