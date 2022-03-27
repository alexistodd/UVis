from picamera import PiCamera
from time import sleep

#picamera library
camera = PiCamera()

#start camera view fullscreen
camera.start_preview()
sleep(5)

#change strasnaprency of camera
#view until gone completeley
camera.start_preview(alpha=200)
sleep(5)
camera.start_preview(alpha=150)
sleep(5)
camera.start_preview(alpha=100)
sleep(5)
camera.start_preview(alpha=50)
sleep(5)
camera.start_preview(alpha=0)