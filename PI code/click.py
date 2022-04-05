import os
import pygame
from picamera import PiCamera
from time import sleep

#picamera library
camera = PiCamera()
#pygame application window
pygame.init()
window = pygame.display.set_mode((800,480))
#pygame.display.toggle_fullscreen()
pygame.display.set_caption("Touchscreen Detection")

#start camera view fullscreen
camera.start_preview()

#default brightness is 50
camera.brightness = 70
camera.rotation = 180
#it’s important to sleep for at least
#two seconds before capturing an image,
#because this gives the camera’s sensor time to
#sense the light levels.
sleep(2)

mainloop=True
while mainloop:

    pygame.time.delay(10)
    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            mainloop=False

        #detects single tap from touchscreen
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            #capture image 
            camera.capture('/home/pi/Desktop/images/image.jpg')
            #stop preview
            camera.stop_preview()
            #show image fullscreen using feh
            os.system("feh -F --on-last-slide quit /home/pi/Desktop/images")
            #restart preview behind the image
            #after screen tap the video feed will already be loaded
            camera.start_preview()    

pygame.quit()
