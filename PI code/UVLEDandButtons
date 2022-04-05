import threading
import os
import sys
import time
import RPi.GPIO as GPIO

# ================== FUNCTIONS ===================== #
def check_debug():       
    while(True):
        if(GPIO.input(debugButton) == 0):
             print("Debug button pressed: exiting program")
             os.system('sudo shutdown now')
        
def check_lights():
    lightOn = False
    while(True):
        if(GPIO.input(lightButton) == 0):
            if lightOn == False:
                GPIO.output(lightPin1,0)
                GPIO.output(lightPin2,0)
                lightOn = True;
                time.sleep(0.15)
            else:
                GPIO.output(lightPin1,1)
                GPIO.output(lightPin2,1)
                lightOn = False;
                time.sleep(0.15)

def run_camera():
#     resolution of lcd screen is 800x400
    os.system('libcamera-vid -t 15000 --width 800 --height 400 --fullscreen')        
    
def setup_background_threads():
    light = threading.Thread(target=check_lights, daemon=True)
    light.start()

    debug = threading.Thread(target=check_debug, daemon=True)
    debug.start()

    
# ================== DEFINITIONS ===================== # 

# LED light pins
lightPin1 = 5
lightPin2 = 6

# button pins
button_vcc = 13
lightButton = 19
debugButton = 26
#powerPin = 21

exit_program = 0

# ================== MAIN ===================== # 
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    # Set the pins to inputs or outputs 
    GPIO.setup(lightPin1, GPIO.OUT)
    GPIO.setup(lightPin2, GPIO.OUT)
    GPIO.setup(button_vcc, GPIO.OUT)

    GPIO.setup(lightButton, GPIO.IN)
    GPIO.setup(debugButton, GPIO.IN)

    GPIO.output(lightPin1, 0)
    GPIO.output(lightPin2, 0)
    GPIO.output(button_vcc, 1)

    setup_background_threads()
    
        
    camera = threading.Thread(target=run_camera)
    camera.start()
    
    while(True):
        pass
