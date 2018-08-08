from sense_hat import SenseHat
from time import time, sleep
import os
import sys
from random import randint

# constants
TEXT = 'Hello! We are New Media Development :)'
SPEED = 0.1

# get random color
def get_random_color():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)

    return (random_red, random_green, random_blue)

try:
    # SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)
    
def main():
    while True:
        sense_hat.show_message(text_string=TEXT, text_colour=get_random_color(), back_colour=get_random_color(), scroll_speed=SPEED)
        sense_hat.clear()
        
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sense_hat.clear()
        sys.exit(0)
