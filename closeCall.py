
#Libraries
import RPi.GPIO as GPIO
import time
from picamera import PiCamera, Color
from time import sleep
from datetime import datetime
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set GPIO Pins
TRIG = 23 
ECHO = 24
 
print ("Distance Measurement In Progress")
#set GPIO direction (IN / OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#set camera
camera = PiCamera()
camera.start_preview(alpha=200)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(TRIG, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance =((TimeElapsed * 34300) / 2) / 100
 
    return distance 
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.3f m" % dist)
            if dist < 1:
                for i in range (3):
                    fileName = datetime.now().strftime('/home/pi/Desktop/camera/project/%Y-%m-%d_%H.%M.%S.jpg')
                    camera.capture(fileName)
                    print('photo captured')
                    time.sleep(1)
            else:
                time.sleep(3)

 
#Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        camera.stop_preview()



