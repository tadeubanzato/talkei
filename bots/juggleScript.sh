#!/bin/sh
weekDay=$(date +"%u")
timeDay=$(date +"%H")


if [ $timeDay -ge 5 -a $timeDay -le 7 ]; then
  sudo pkill -f minions.py
  sudo pkill -f fav_retweet.py
  export L="FavRetweet"
  #python3 ping_runing.py "$L" &
  python3 fav_retweet.py &
else
  if [ $timeDay -ge 7 -a $timeDay -le 9 ]; then
    sudo pkill -f minions.py
    sudo pkill -f fav_retweet.py
    export L="Minions"
    #python3 ping_runing.py "$L" &
    python3 minions.py &
  else
    if [ $timeDay -ge 9 -a $timeDay -le 11 ]; then
      sudo pkill -f minions.py
      sudo pkill -f fav_retweet.py
      export L="FavRetweet"
      #python3 ping_runing.py "$L" &
      python3 fav_retweet.py &
    else
      if [ $timeDay -ge 11 -a $timeDay -le 13 ]; then
        sudo pkill -f minions.py
        sudo pkill -f fav_retweet.py
        export L="FavRetweet"
        #python3 ping_runing.py "$L" &
        python3 minions.py &
      else
        if [ $timeDay -ge 13 -a $timeDay -le 15 ]; then
          sudo pkill -f minions.py
          sudo pkill -f fav_retweet.py
          export L="FavRetweet"
          #python3 ping_runing.py "$L" &
          python3 fav_retweet.py &
        else
          if [ $timeDay -ge 15 -a $timeDay -le 17 ]; then
            sudo pkill -f minions.py
            sudo pkill -f fav_retweet.py
            export L="FavRetweet"
            #python3 ping_runing.py "$L" &
            nohup python3 minions.py &
          else
            if [ $timeDay -ge 17 -a $timeDay -le 19 ]; then
              sudo pkill -f minions.py
              sudo pkill -f fav_retweet.py
              export L="FavRetweet"
              #python3 ping_runing.py "$L" &
              python3 fav_retweet.py &
            else
              if [ $timeDay -ge 19 -a $timeDay -le 20 ]; then
                sudo pkill -f minions.py
                sudo pkill -f fav_retweet.py
                export L="FavRetweet"
                #python3 ping_runing.py "$L" &
                python3 minions.py &
              else
                if [ $timeDay -ge 21 -a $timeDay -le 22 ]; then
                  sudo pkill -f minions.py
                  sudo pkill -f fav_retweet.py
                  export L="FavRetweet"
                  #python3 ping_runing.py "$L" &
                  python3 fav_retweet.py &
                else
                  if [ $timeDay -ge 22 -a $timeDay -le 23 ]; then
                    sudo pkill -f minions.py
                    sudo pkill -f fav_retweet.py
                    export L="FavRetweet"
                    #python3 ping_runing.py "$L" &
                    python3 minions.py &
                  else
                    if [ $timeDay -ge 23 -a $timeDay -le 5 ]; then
                      sudo pkill -f fav_retweet.py
                      sudo pkill -f minions.py
                    fi
                  fi
                fi
              fi
            fi
          fi
        fi
      fi
    fi
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


# -eq # equal
# -ne # not equal
# -lt # less than
# -le # less than or equal
# -gt # greater than
# -ge # greater than or equal
# ps command: ps aux | grep file named
