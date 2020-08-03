# PiMonitor
This is my Raspberry Pi project.

My task was to create a system where a Raspberry Pi could provide the following metrics on an internal webpage. I'm a SysAdmin and not a developer so I'm sure there are more efficient ways to program this (I.E. not using bash scripts in cron to launch the python scripts but I got it working the way it is so I left it. My time budget ran out from the project but I may change it later).

1. Intrusion detection
  (Email alert on sensor change state)
2. Environmental Monitoring
3. Regular internet speed tests
4. Monitoring of the Raspberry Pi statistics.

This is the the hardware I used to create the setup

Required:
1. Cana Kit Raspberry Pi 4 8gb (Which is way overkill and significant modification to the supplies case via Dremel is required but it will all fit in the case)
  (https://smile.amazon.com/gp/product/B08956GVXN/ref=ppx_yo_dt_b_asin_title_o01_s01?ie=UTF8&psc=1)
2. DHT11 (temperature and humidity monitor)
  (https://smile.amazon.com/gp/product/B07T7ZR7MS/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1)
3. Surface Mount Alarm 10W 100V 0.5A (not sure if the specific eleictral specs matter, I did not use them to base them on my purchase I just bought surface mount alarm switches)
  (https://smile.amazon.com/gp/product/B07F314V3Z/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

Optional:
1. PCB Breadboard (makes it cleaner to solder the wires to the board and makes it more permanant)
  (https://smile.amazon.com/gp/product/B07MCX54ZD/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)
2. 1/4" Wire Sleeving
  (https://smile.amazon.com/gp/product/B071JH14WZ/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)
3. Shrink Tubing
  (https://smile.amazon.com/gp/product/B07T4SYVYG/ref=ppx_yo_dt_b_asin_image_o05_s00?ie=UTF8&psc=1)
4. Wire for cable extensions
  (https://smile.amazon.com/gp/product/B07T4SYVYG/ref=ppx_yo_dt_b_asin_image_o05_s00?ie=UTF8&psc=1)
    
Next is the required software:

1. Raspberry Pi OS 10 (Buster) Lite (No GUI required)
  (https://www.raspberrypi.org/downloads/raspberry-pi-os/)
2. Apache2
  (sudo apt-get install apache2 -y)
3. Python & python3
  (sudo apt install python3-pip)
  (sudo apt install python-pip)
4. Git
  (apt-get install git)
5. vcgencmd (is included with OS)
6. speedtest-cli
  (sudo pip install speedtest-cli)
  
Results:
  
Here is the resulting web page
https://i.imgur.com/rvLknKA.png

