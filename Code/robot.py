from adafruit_servokit import ServoKit
import camera
from time import sleep

''' PIN MAP:
    [0] is tail
    [1] is mid-tail
    [2] is hip
    [3] is mid-head
    [4] is head
    [5] is suction cup
'''


class Robot:
    def __init__(self):
        self.cam = camera.Camera()
        self.kit = ServoKit(channels=16)
        self.kit.servo[0].angle = 90
        self.kit.servo[1].angle = 90
        self.kit.servo[2].angle = 90
        self.kit.servo[3].angle = 90
        self.kit.servo[4].angle = 90
        self.kit.servo[5].angle = 90

        self.stuck = False

    def _stick(self):
        self.kit.servo[5] = 45
        self.stuck = True

    def _unstick(self):
        self.kit.servo[5] = 90
        self.stuck = False

    def _curl_up(self):
        # STUB TODO
        return

    def _extend(self):
        self.kit.servo[0].angle = 90
        self.kit.servo[1].angle = 90
        self.kit.servo[2].angle = 90
        self.kit.servo[3].angle = 90
        self.kit.servo[4].angle = 90

    def crawl(self):
        self._stick()
        self._curl_up()
        self._unstick()
        self._extend()

    def turn(self, degrees):
        while degrees > 45 or degrees < -45:
            if degrees > 45:
                self.turn(45)
                degrees -= 45
            elif degrees < -45:
                self.turn(-45)
                degrees += 45

        self.kit.servo[2].angle = 90 + degrees
        self._stick()
        self.kit.servo[2].angle = 90
        self._unstick()

    def suction(self):
        if self.stuck:
            self._unstick()
        else:
            self._stick()

    def sees_blue(self):
        return self.cam.sees_blue()