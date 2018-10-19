# Event: nmd_doors_open_or_close
# Documentation: https://ifttt.com/services/maker_webhooks/settings
# Settings: https://ifttt.com/services/maker_webhooks/settings
# Connection: https://maker.ifttt.com/use/c9KgUA_naJd3ZDRJbFb26t
# Test URL: curl -X POST https://maker.ifttt.com/trigger/nmd_doors_open_or_close/with/key/c9KgUA_naJd3ZDRJbFb26t'
# Library: pip3 install requests
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep
import requests
import time
import json
from signal import pause

headers_json = {
    'Content-type': 'application/json',
    'Accept': 'text/plain'
}

def launchIFTTTWebRequest(door, state):
    data = {
        'value1': door,
        'value2': state
    }
    r = requests.post('https://maker.ifttt.com/trigger/nmd_doors_open_or_close/with/key/c9KgUA_naJd3ZDRJbFb26t', data=json.dumps(data), headers=headers_json)
    print('Sent request to IFTTT Webhook')

def pushed_up(event):
    if event.action != ACTION_RELEASED:
        launchIFTTTWebRequest('front', 'opened')

def pushed_down(event):
    if event.action != ACTION_RELEASED:
       launchIFTTTWebRequest('front', 'closed')

def pushed_left(event):
    if event.action != ACTION_RELEASED:
        launchIFTTTWebRequest('back', 'opened')

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        launchIFTTTWebRequest('back', 'closed')
    
sense_hat = SenseHat()
sense_hat.stick.direction_up = pushed_up
sense_hat.stick.direction_down = pushed_down
sense_hat.stick.direction_left = pushed_left
sense_hat.stick.direction_right = pushed_right
pause()