from sense_hat import SenseHat
from time import time, sleep
import sys

# constants
BK = (0,0,0)
WH = (255,255,255)
RD = (255, 0, 77)
BL = (41, 173, 255)
BR = (187, 90, 59)
PK = (255, 208, 174)
YL = (250, 252, 44)

MARIO = [
    BK, BK, BK, RD, RD, RD, WH, BK,
    BK, BK, BK, RD, RD, RD, RD, RD,
    BK, BK, BR, PK, BR, BK, PK, BK,
    BK, BK, BR, PK, PK, BR, BR, PK,
    BK, BK, BK, BR, PK, PK, PK, BK,
    BK, RD, RD, YL, BL, BL, YL, BK,
    WH, BK, BL, BL, BL, BL, BK, BL,
    BK, BK, BR, BK, BK, BK, RD, BK  
    
]

MARIO_JUMP = [
    BK, BK, BK, RD, RD, RD, RD, RD,
    BK, BK, BR, PK, BR, BK, PK, BK,
    BK, BK, BR, PK, PK, BR, BR, PK,
    BK, BK, BK, BR, PK, PK, PK, BK,
    WH, RD, BL, YL, BL, BL, YL, BL,
    BK, BK, BR, BK, BK, BK, RD, BK,  
    BK, BK, BK, BK, BK, BK, BK, BK,   
    BK, BK, BK, BK, BK, BK, BK, BK    
]

try:
    # SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)
    
def main():
    jump = False
    
    while True:        
        if jump:
          sense_hat.set_pixels(MARIO_JUMP)
        else:
          sense_hat.set_pixels(MARIO)
          
        sleep(1)
        
        jump = not jump
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
