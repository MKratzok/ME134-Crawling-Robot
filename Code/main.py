import robot
import sys
from time import sleep


def run_auto(r):
    """
    run_auto(r) - The robot will crawl until it sees blue and then turn 180 degrees and crawl the same distance again
    :param r: a robot class
    :return: nothing
    """

    print("   ___________________________________")
    print("  /                                  /")
    print(" /            AUTO MODE             /")
    print("/__________________________________/")

    steps = 0

    for i in range(0, 20):
        r.crawl()
        sleep(0.5)

    while not r.sees_blue():
        r.crawl()
        sleep(0.5)

    r.turn(3960)

    for i in range(0,10):
        r.crawl()
        sleep(0.5)

    while not r.sees_blue():
        r.crawl()
        sleep(0.5)

    r.dance(10)


def run_manual(r):
    """
    run_manual(r) - Gives user control of robot until they quit. Control with WASD keys
    :param r: a robot class
    :return: nothing
    """
    #if extra time, then use arrow keys/don't press enter

    print("   ___________________________________")
    print("  /                                  /")
    print(" /           MANUAL MODE            /")
    print("/__________________________________/")

    sleep(1)

    c = ""

    while c.lower() != "q":
        c = input().lower()

        if c == "w":
            r.crawl()
        elif c == "d":
            r.turn(-90)
        elif c == "a":
            r.turn(90)
        elif c == "s":
            r.suction()
        elif c == "c":
            r.sees_blue()
        elif c == "!":
            r.dance(10)
        elif c != "q":
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