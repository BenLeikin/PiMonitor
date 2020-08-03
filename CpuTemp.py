#!/usr/bin/env python

import os #imports the native commands to read the cpu temp
import time #imports the clock

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline() #reads the temp from the built-in command vcgenmc
        return (temp.replace("temp=","")) #outputs the formatted Temp reading

while True:
        text_file = open("CpuTemp.txt", "w") #opens the text file for outputting to the webpage
        text_file.write(measure_temp()) #writes the temp
        text_file.close() #closes the text file
        time.sleep(2) #refreshes every 1 second
