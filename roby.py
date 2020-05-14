from gpiozero import Robot
import subprocess as s
#import recog
robby = Robot(left=(9,10), right=(7,8))

def arranca():
    while True:
        robby.forward()
        #sleep(5)
#         robby.stop()

def stop():
    while True:
        robby.stop()