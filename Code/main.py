import robot

def run_auto(r): #todo
    while True:
        r.crawl()
        if r.do_camera_stuff():
            r.turn(180)

    #Go forward until camera detects tape then turn and return

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
    # get cmd line argument for auto or manual mode  todo
    auto = False

    r = robot.Robot()

    if auto:
        run_auto(r)
    else:
        run_manual(r)


'''todo list:
    1) add camera code - J
    2) run auto (depends on camera) 
    3) get cmd line arg for auto mode - M
    4) figure out how much to "curl up" 
    5) figure out how much servo should move to stick/unstick'''