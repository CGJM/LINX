from gpiozero import Robot
import subprocess as s
#import recog
robby = Robot(left=(9,10), right=(7,8))

def arranca():
    while True:
        robby.forward()
        sleep(5)
        robby.stop()

def right():
    while True:
        robby.right()
        sleep(5)
        robby.stop()

def left():
    while True:
        robby.left()
        sleep(5)
        robby.stop
