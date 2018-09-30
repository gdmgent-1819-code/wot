# Copyright 2019 New Media Development
#
# Website: http://www.gdm.gent
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from sense_hat import SenseHat
from time import time, sleep
import subprocess
import os
import sys

serviceAccountKey = '../../../../../keys/wot-1819-firebase-adminsdk-rdty1-0f1422347a.json'
databaseURL = 'https://wot-1819.firebaseio.com'

def get_sensehat_temp():
    process = subprocess.Popen('sudo python3 sensehat_temperature.py True', shell=True, stdout=subprocess.PIPE)
    (output, err) = process.communicate()
    process_status = process.wait()
    temp_str = str(output).replace("b'", "").replace("\\n'", "")
    temp = float(temp_str)    
    return(temp)

try:
    # Fetch the service account key JSON file contents
    firebase_cred = credentials.Certificate(serviceAccountKey)

    # Initalize the app with a service account; granting admin privileges
    firebase_admin.initialize_app(firebase_cred, {
    'databaseURL': databaseURL
    })

    # As an admin, the app has access to read and write all data
    firebase_ref_pi_sensehat_environment_sensors = db.reference('pi-sensehat-environment-sensors')
except:
    print('Unable to initialize Firebase: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

try:
    # SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)
    
def main():
    while True:
        #temperature = round(sense_hat.get_temperature())
        temperature = round(get_sensehat_temp())
        humidity = round(sense_hat.get_humidity())
        pressure = round(sense_hat.get_pressure())
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure
        }
        firebase_ref_pi_sensehat_environment_sensors.push().set(data)
        sleep(60)
        
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)



    


