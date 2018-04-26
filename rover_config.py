import requests
import time, sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.output(20, 0)  # turn on
GPIO.output(21, 0)  # turn on
GPIO.output(26, 0)  # turn on
time.sleep(0.5)
#conecta hokuyo
GPIO.output(20, 1)  # turn off
GPIO.output(21, 1)  # turn off
GPIO.output(26, 1)  # turn off
time.sleep(0.2)
GPIO.output(20, 0)  # turn on
GPIO.output(21, 0)  # turn on
GPIO.output(21, 0)  # turn on
time.sleep(0.2)
# conecta pololu
GPIO.output(20, 1)  # turn off
GPIO.output(21, 1)  # turn off
GPIO.output(26, 1)  # turn off
time.sleep(0.2)
GPIO.output(20, 0)  # turn on
GPIO.output(21, 0)  # turn on
GPIO.output(21, 0)  # turn on
time.sleep(0.2)
#conecta roboclaw
GPIO.output(20, 1)  # turn off
GPIO.output(21, 1)  # turn off
GPIO.output(26, 1)  # turn off
time.sleep(0.2)
GPIO.output(20, 0)  # turn on
GPIO.output(21, 0)  # turn on
GPIO.output(21, 0)  # turn on

sys.exit()
