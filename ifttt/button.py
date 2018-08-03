# Event: nmd_wot_button_pressed
# Documentation: https://ifttt.com/services/maker_webhooks/settings
# Settings: https://ifttt.com/services/maker_webhooks/settings
# Connection: https://maker.ifttt.com/use/c9KgUA_naJd3ZDRJbFb26t
# Test URL: curl -X POST https://maker.ifttt.com/trigger/nmd_wot_button_pressed/with/key/dNKChU0OqeQvY2s-SJO3ed
'''
drdynscript@MacBook-Pro-van-Philippe:~/ahs/gdm/gdmgent-1819-code/wot/ifttt$ curl -X POST https://maker.ifttt.com/trigger/nmd_wot_button_pressed/with/key/dNKChU0OqeQvY2s-SJO3ed
Congratulations! You've fired the nmd_wot_button_pressed eventdrdynscript@MacBook-Pro-van-Philippe:~/ahs/gdm/gdmgent-1819-code/wot/ifttt$
'''
# Library: pip3 install requests
from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep
import requests
import time
import json
import platform

headers_json = {
    'Content-type': 'application/json',
    'Accept': 'text/plain'
}

def launchIFTTTWebRequest():
    data = {
        'value1': time.time(),
        'value2': platform.uname()[1]
    }
    r = requests.post('https://maker.ifttt.com/trigger/nmd_wot_button_pressed/with/key/dNKChU0OqeQvY2s-SJO3ed', data=json.dumps(data), headers=headers_json)
    print('Sent request to IFTTT Webhook')
    
sense = SenseHat()

while True:
    event = sense.stick.wait_for_event()
    if event.action == 'pressed' and event.direction == 'middle':
        print("The joystick was {} {}".format(event.action, event.direction))
        launchIFTTTWebRequest()
        
    sleep(0.1)
