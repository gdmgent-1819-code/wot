# Library: sudo pip3 install 'pubnub>=4.1.0'
# Event: nmd_wot_button_pressed
# Documentation: https://ifttt.com/services/maker_webhooks/settings
# Settings: https://ifttt.com/services/maker_webhooks/settings
# Connection: https://maker.ifttt.com/use/c9KgUA_naJd3ZDRJbFb26t
from sense_hat import SenseHat
from time import sleep
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import json
import platform

pnconfig = PNConfiguration()

pnconfig.publish_key = 'pub-c-7a9982ea-c39a-4d66-b1ca-1c5138235ec7' 
pnconfig.subscribe_key = 'sub-c-857c7620-9722-11e8-979a-3665db0876c0'

pubnub = PubNub(pnconfig)

class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data
 
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass  # This event happens when radio / connectivity is lost
 
        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            pass
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
            pass
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.
            pass
 
    def message(self, pubnub, message):
        pass  # Handle new message stored in message.message
 
 
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('ledChannel').execute()
