import P3picam
import picamera
from urllib.request import urlopen
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email import encoders
import re
from datetime import datetime
from subprocess import call

COMMASPACE = ','
motionState = False
picPath = "/home/pi/Desktop/cookie/images/"
count=1
from_address= 'punyaslokduttaraspberrypi@gmail.com'
to_address= 'punyaslokduttaraspberrypi@gmail.com'
subject= 'Raspberrypi Security Camera'
username= 'punyaslokduttaraspberrypi'
password= '########'
command2="rm -r images/*"
call([command2], shell=True)

def send_email(picName):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    body = picName + "has been DETECTED"
    msg.attach(MIMEText(body, 'plain'))
    
    filename=  picPath + picName
    print(filename)
    attachment = open(filename, 'rb').read()
    image= MIMEImage(attachment, name=os.path.basename(picName))
    msg.attach(image)
    s= smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(username,password)
    text=msg.as_string()
    s.sendmail(from_address, to_address, text)
    s.quit()
    print("Our Email is sent!")
def captureImage(currentTime, picPath, count):
    # Generate the picture's name
    picName = str(count) + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
    print("We have taken a picture.")
    return picName

def getTime():
    # Fetch the current time
    currentTime = datetime.now()
    return currentTime

def timeStamp(currentTime, picPath, picName):
    # Variable for file path
    filepath = picPath + picName
    # Create message to stamp on picture
    message = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    # Create command to execute
    timestampCommand = "/usr/bin/convert " + filepath + " -pointsize 36 \
    -fill red -annotate +700+650 '" + message + "' " + filepath
    # Execute the command
    call([timestampCommand], shell=True)
    print("We have timestamped our picture.")

while True:
    motionState = P3picam.motion()
    print(motionState)
    if motionState:
        currentTime = getTime()
        picName = captureImage(currentTime, picPath, count)
        count+=1
        timeStamp(currentTime, picPath, picName)
        send_email(picName)
        
