import picamera
import time
#To set the camera
print("Picture is about  to be Taken")
print("Click")
with picamera.PiCamera() as camera:
    camera.resolution=(1280, 720)
    camera.capture('/home/pi/Desktop/cookie/newimage.jpg')
    camera.stop_preview()
print("Picture Taken")
    
