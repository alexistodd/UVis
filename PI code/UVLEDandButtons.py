import threading
import os
import sys
import time
import RPi.GPIO as GPIO
import pygame
from picamera import PiCamera

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
                lightOn = True;
                time.sleep(0.15)
            else:
                GPIO.output(lightPin1,1)
                lightOn = False;
                time.sleep(0.15)

# def check_touchscreen():
    # global running 
    
    # while(True):
        # if(running):
            # pygame.time.delay(10)
            # for event in pygame.event.get():
                # if event.type == pygame.QUIT:
                    # running = False 
                    
            # # detects single tap from touchscreen              
            # if event.type==pygame.MOUSEBUTTONDOWN:
                
                # # capture image 
                # camera.capture('/home/pi/Desktop/images/image.jpg')
                
                # # stop preview
                # camera.stop_preview()
                
                # # show image fullscreen using feh
                # os.system("feh -F --on-last-slide quit /home/pi/Desktop/images")
                
                # #restart preview behind the image
                # #after screen tap the video feed will already be loaded
                # camera.start_preview()   
            
    
# def run_camera(camera):
    
    
def setup_background_threads():
    light = threading.Thread(target=check_lights, daemon=True)
    light.start()

    debug = threading.Thread(target=check_debug, daemon=True)
    debug.start()
    
    #touchscreen = threading.Thread(target=check_touchscreen, daemon=True)
    
   #touchscreen.start()

    
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

# Loop condition 
global running 
running = False 



# GPIO INIT 
GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin1, GPIO.OUT)

GPIO.setup(lightButton, GPIO.IN)
GPIO.setup(debugButton, GPIO.IN)

GPIO.output(lightPin1, 0)

# CAMERA INIT 
camera = PiCamera()
camera.brightness = 70

# TOUCHSCREEN INIT
pygame.init()
window = pygame.display.set_mode((800,400))
pygame.display.set_caption("Touchscreen Detection")


# ================== MAIN ===================== # 
# THREAD STARTS  
setup_background_threads()  

camera.start_preview()

running = True

while(running):       
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
    # detects single tap from touchscreen              
    if event.type==pygame.MOUSEMOTION:
        
        # capture image 
        camera.capture('/home/pi/Desktop/images/image.jpg')
        
        # stop preview
        camera.stop_preview()
        
        # show image fullscreen using feh
        os.system("feh -F --on-last-slide quit /home/pi/Desktop/images")
        
        #restart preview behind the image
        #after screen tap the video feed will already be loaded
        camera.start_preview()

pygame.quit()            
        






