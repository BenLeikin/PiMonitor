#!/usr/bin/env python3

import RPi.GPIO as GPIO #imports the GPIO library to get readings from the GPIO pins
import dht11 #this is the physcal temp/humidity device
import time #imports the clock

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin = 4)

while True:  
        result = instance.read() #while the DHT11 is detected it reads the values
        #opens the text file, formates the output, and then writes it for output to the webpage and then closes it
        text_file = open("/home/pi/EnvMonitorStatus.txt", "w")
        text_file.write("Temperature: %-3.1fC" % result.temperature)
        text_file.write(" Humidity: %-3.1f%%" % result.humidity)
        text_file.close()
        time.sleep(5) #refreshes every 5 seconds
