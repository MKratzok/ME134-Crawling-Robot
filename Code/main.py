import robot
import sys
from time import sleep


def run_auto(r):
    """
    run_auto(r) - The robot will crawl until it sees blue and then turn 180 degrees and crawl the same distance again
    :param r: a robot class
    :return: nothing
    """

    steps = 0
    while True:
        r.crawl()
        steps += 1

        if r.sees_blue():
            r.turn(180)
            # for i in range(0,steps)
            #     r.crawl()

        sleep(1)


def run_manual(r):
    """
    run_manual(r) - Gives user control of robot until they quit. Control with WASD keys
    :param r: a robot class
    :return: nothing
    """
    #if extra time, then use arrow keys/don't press enter
    c = ""

    while c.lower() != "q":
        c = input().lower()

        if c == "w":
            r.crawl()
        elif c == "d":
            r.turn(45)
        elif c == "a":
            r.turn(-45)
        elif c == "s":
            r.suction()
        else:
            print(c + ': Command not found')

        sleep(0.1)


if __name__ == "__main__":
    if len(sys.argv) is 1:
        auto = False
    elif sys.argv[1] in ['--auto', '-a']:
        auto = True
    elif sys.argv[1] in ['--manual', '-m']:
        auto = False
    else:
        print('usage: main.py [-a or --auto] or [-m --manual]')
        quit()

    r = robot.Robot()

    if auto:
        run_auto(r)
    else:
        run_manual(r)


'''todo list:
    4) figure out how much to "curl up" 
    5) figure out how much servo should move to stick/unstick'''