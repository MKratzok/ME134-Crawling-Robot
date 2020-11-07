import robot
import sys


def run_auto(r): #todo
    while True:
        r.crawl()
        if r.sees_blue():
            r.turn(180)


def run_manual(r):
    #if extra time, then use arrow keys/don't press enter
    c = ""

    while c.lower() is not 'q':
        c = input().lower()

        if c is 'w':
            r.crawl()
        elif c is 'd':
            r.turn(45)
        elif c is 'a':
            r.turn(-45)
        elif c is 's':
            r.suction()


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