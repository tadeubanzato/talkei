#!/bin/sh

var1=`ps -ef | grep -v grep | grep minions_scrapping2.py | awk '{print $2}'`
echo $var1
if [ -n $var1 ]
then
echo "The Process is Running"
else
echo "Starting process"
python3 /home/pi/talkei/bots/minions_scrapping2.py &
fi
