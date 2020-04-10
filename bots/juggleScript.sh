#!/bin/sh
weekDay=$(date +"%u")
timeDay=$(date +"%H")


if [ $timeDay -ge 5 -a $timeDay -le 12 ]; then
  sudo pkill -f minions.py
  nohup python3 /home/pi/talkei/bots/fav_retweet.py  &
else
  if [ $timeDay -ge 12 -a $timeDay -le 18 ]; then
    sudo pkill -f fav_retweet.py
    export L="FavRetweets"
    exec python3 ping_runing.py "$L"
    nohup python3 /home/pi/talkei/bots/minions.py  &
  fi
fi


# if [ $weekDay -eq 6 -o $weekDay -eq 7 ]; then
#     DISPLAY=:0 xset dpms force off
#     sudo python /home/pi/ping_Sleep.py &
# else
#   if [ $timeDay -ge 7 -a $timeDay -le 18 ]; then
#     DISPLAY=:0 xset dpms force on
#     sudo python /home/pi/ping_awake.py &
#   else
#     DISPLAY=:0 xset dpms force off
#     sudo python /home/pi/ping_sleep.py &
#   fi
# fi


#-eq # equal
#-ne # not equal
#-lt # less than
#-le # less than or equal
#-gt # greater than
#-ge # greater than or equal
#ps command: ps aux | grep file named
