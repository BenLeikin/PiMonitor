#!/bin/bash

# This file allows the cron job to run from a .sh file rather than the python file (was having issues having it run the python script)
cd / #navigates to /home/pi where the scripts are located
cd /home/pi/
sudo python CpuTemp.py #runs the python script
