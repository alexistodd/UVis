# Start the camera when the pi turns on in fullscreen mode with width
# and height that matches the LCD Display
#import os

#os.system('libcamera-vid -t 10000 --fullscreen --width 800 --height 480')

# Button input
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

# sleeptimer
sleepTime = 0.1

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

lightOn = False

while True:
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
#     GPIO.output(lightPin1, GPIO.input(lightButton))
#     GPIO.output(lightPin2, GPIO.input(lightButton))
    sleep(sleepTime)
    
    
