import picamera
from time import sleep
from subprocess import call
#setting up camera
with picamera.PiCamera() as camera:
    #start recording
    camera.start_recording("pythonVideo.h264")
    sleep(5)
    camera.stop_recording()
print("Video to be Converted")
command="MP4Box -add pythonVideo.h264 convertedVideo.mp4"
call([command], shell=True)
print("Video Converted")
