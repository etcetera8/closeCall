Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import RPi.GPIO as GPIO
>>> import time
>>> 
>>> GPIO.setmode(GPIO.BCM)
>>> 
>>> GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
>>> 
>>> while True:
	input_state = GPIO.input(18)
	if input_state == False:
		print('button pressed')
		time.sleep(0.2)
