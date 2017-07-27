
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
picPath = "/root/Desktop/cookie/images/"
from_address= 'punyaslokduttaraspberrypi@gmail.com'
to_address= 'punyaslokduttaraspberrypi@gmail.com'
subject= 'Raspberrypi Security Camera'
username= 'punyaslokduttaraspberrypi'
password= '######'
picName= 'ss.jpg'

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
send_email(picName)
