from time import sleep
import sys
import os
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.load_image('./images/space_invader.png')

while True:
  try:
    sleep(1)

  except KeyboardInterrupt:
    print('Interrupted')
    sense.clear()
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

sense.clear()