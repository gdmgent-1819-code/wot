from sense_hat import SenseHat
from time import time, sleep
import os
import sys
from random import randint

# constants
M_ROWS = 7
M_COLS = 7
M_CLEAR_BEFORE_LOOP = True

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
        x_pos = 0
        y_pos = 0

        while (y_pos <= M_ROWS):
            if M_CLEAR_BEFORE_LOOP:
                sense_hat.clear()
                
            sense_hat.set_pixel(x_pos, y_pos, get_random_color())
            sleep(0.1)
            
            y_pos = (y_pos + 1) if (x_pos + 1 == M_COLS + 1) else (y_pos)
            x_pos = (x_pos + 1) if (x_pos + 1 <= M_COLS) else (0)

        sleep(2)
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
