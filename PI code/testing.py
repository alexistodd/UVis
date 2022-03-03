import threading
import os
import time
import os
import RPi.GPIO as GPIO
    
def check_lights():
    lightOn = False
    while(True):
        if(GPIO.input(lightButton) == 1):
            if(lightOn == True):            
                GPIO.output(lightPin1, 0)
                GPIO.output(lightPin2, 0)
                while(lightButton == True):
                    sleep(sleepTime)
                lightOn = False
            else:
                GPIO.output(lightPin1, 1)
                GPIO.output(lightPin2, 1)
                while(lightButton == True):
                    sleep(sleepTime)
                lightOn = True
        time.sleep(0.1)

GPIO.setmode(GPIO.BCM)

# LED light pins
lightPin1 = 16
lightPin2 = 12

# Light button pins
lightButton = 20
powerPin = 21

# Set the pins to inputs or outputs 
GPIO.setup(lightPin1, GPIO.OUT)
GPIO.setup(lightPin2, GPIO.OUT)
GPIO.setup(lightButton, GPIO.IN)#, pull_up_down=GPIO.PUD_UP) # set to pull up
GPIO.setup(powerPin, GPIO.OUT)

GPIO.output(powerPin, 1)
GPIO.output(lightPin1, 0)
GPIO.output(lightPin2, 0)

light = threading.Thread(target=check_lights, daemon=True)
light.start()

# while(True):
#     pass
os.system('libcamera-vid -t 10000 --fullscreen --width 800 --height 480 ')

