!/usr/bin/env python

import RPi.GPIO as GPIO #imports the GPIO library
import time #imports the clock
import smtplib #imports the email library

GPIO.setmode(GPIO.BOARD) #sets the mode of the GPIO board (this reads the pin value rather than the GPIO value. If you refer to EnvMonitory.py that script 
#reads from the GPIO pin value
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #tells the system to read from GPIO pin 11

#Email message 
#Bug: Cannot get the subject or the sender of the email to be displayed
def send_alert(doorstate):

        sender = 'laxpi@tollfreeforwarding.com'
        receivers = ['bl@tollfreeforwarding.com']

        message = """From: LAX Pi <laxpi@tollfreeforwarding.com>
        To: BL <bl@tollfreeforwarding.com>
        Subject: ALERT: The status of the REAR cabinet door in LAX has changed 

        This is a notification that the REAR cabinet door in LAX is """ +DoorRear

        try:
                smtpObj = smtplib.SMTP('10.20.1.126')
                smtpObj.sendmail(sender, receivers, message)
        except: 
                print ("Ben was here")


#while loop to determine if the door is open or closed
while True:
        if GPIO.input(16): #states the door state open or closed
                DoorRear = "Open"
        else:
                DoorRear = "Closed"

#opens the text file, compares the previous state of the door, writes the formatted status of the door to the text file, and then closes the file
        text_file = open("/home/pi/RearDoorStatus.txt", "r")
        old_text_value = text_file.read()
        text_file.close()
        old_text_value = old_text_value.replace('\n','')
        if old_text_value != DoorRear:
                send_alert(DoorRear)
        text_file = open("/home/pi/RearDoorStatus.txt", "w")
        text_file.write(DoorRear)
        text_file.close()
        time.sleep(5) #refreshes every 5 seconds
