import requests
import socket

## IFTTT and Webhook alet
# Array for the values on Webhook ["value1"], ["value2"], etc
report = {}

# Webhook will receive IP address from the pi
report["value1"] = "Starting script: "

# Get DashPi IP address
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
#s.close()
report["value2"] = L

# Resquest post to Webhook integrated with IFTTT
requests.post('https://maker.ifttt.com/trigger/Talkei/with/key/d1oS5w-uq90y8fCs2ot5qG', data=report)
