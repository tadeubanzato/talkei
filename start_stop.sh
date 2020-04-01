#!/bin/sh
weekDay=$(date +"%u")
timeDay=$(date +"%H")

if [ $weekDay -eq 6 -o $weekDay -eq 7 ]; then
    DISPLAY=:0 xset dpms force off
    sudo python /home/pi/ping_Sleep.py &
else
  if [ $timeDay -ge 7 -a $timeDay -le 18 ]; then
    DISPLAY=:0 xset dpms force on
    sudo python /home/pi/ping_awake.py &
  else
    DISPLAY=:0 xset dpms force off
    sudo python /home/pi/ping_sleep.py &
  fi
fi

#-eq # equal
#-ne # not equal
#-lt # less than
#-le # less than or equal
#-gt # greater than
#-ge # greater than or equal
