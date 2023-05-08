import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22, GPIO.IN) #set GPIO 22 as input
    GPIO.setup(24, GPIO.OUT)


def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        ret = 1

    return ret

init()
i = 0
v = i / 10
while True and v < 5:
    switch_pos = read_slide_switch()
    time = 0.05
    while switch_pos == 0 and v < 5:
        i = 0
        v = i / 10
        while v < 5:
            i = 0
            while i < 10:
                GPIO.output(24, 1)
                sleep(time)
                GPIO.output(24, 0)
                sleep(time)
                i += 1
            v += 1
        GPIO.output(24, 0)

    while switch_pos == 1:
        i = 0
        while i < 5:
            GPIO.output(24, 1)
            sleep(time * 2)
            GPIO.output(24, 0)
            sleep(time * 2)
            i += 1
        switch_pos = read_slide_switch()




