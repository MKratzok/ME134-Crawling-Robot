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
        self.kit.servo[3].angle = 80 # calibrated change to 2
        self.kit.servo[4].angle = 100 # CALIBRATED change to 3
        self.kit.servo[5].angle = 80 # Calibrated change to 4

        self.stuck = False

    def _stick(self):
        """
        _stick() - sticks the suction cup
        :return: none
        """
        self.kit.servo[5].angle = 45
        self.stuck = True

    def _unstick(self):
        """
        _unstick() - unsticks the suction cup
        :return: none
        """
        self.kit.servo[5].angle = 90
        self.stuck = False

    def _curl_up(self):
        """
        _curl_up() - arches the inchworm robot's back
        :return: none
        """
        # STUB TODO
        return

    def _extend(self):
        """
        _extend - straightens the inchworm robot's back
        :return: none
        """
        self.kit.servo[0].angle = 90
        self.kit.servo[1].angle = 90
        self.kit.servo[2].angle = 90
        self.kit.servo[3].angle = 90
        self.kit.servo[4].angle = 90

    def crawl(self):
        """
        crawl() - executes the crawl sequence for the robot
        :return: none
        """
        self._stick()
        sleep(0.5)
        self._curl_up()
        sleep(0.5)
        self._unstick()
        sleep(0.5)
        self._extend()
        sleep(0.5)

    def turn(self, degrees):
        """
        turn(degrees) - turns the robot in maximum steps of 45 degrees
        :param degrees: the total number of degrees to turn
        :return: none
        """
        while degrees > 45 or degrees < -45:
            if degrees > 45:
                self.turn(45)
                degrees -= 45
            elif degrees < -45:
                self.turn(-45)
                degrees += 45

            sleep(0.5)

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