#!/bin/bash
screen -dm -S "screen1" /home/pi/talkei/bots/fav_retweet.py
screen -dm -S "screen2" /home/pi/talkei/bots/minion2.py
while true; do
   num_procs=$(pgrep -lf python | wc -l)
   if [ "$num_procs" != "7" ]; then
      pkill python
      screen -dm -S "fail" python script_failed.py
      sleep 10
      pkill python
      screen -dm -S "screen1" /home/pi/talkei/bots/fav_retweet.py
      screen -dm -S "screen2" /home/pi/talkei/bots/minion2.py
   fi
   sleep 20
done
