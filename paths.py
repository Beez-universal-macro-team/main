from functions import *
import time

def canon(rst=True):
    loop = 0

    while True:
        if loop >= 20:
            break

        if rst or loop > 0:
            print("reseting")
            reset()

        time.sleep(0.05)

        press("w", 0.75)

        press("d", 1.1 * (7 - int(readFile("guiFiles/hiveSlot.txt"))))

        keyboard.press("d")

        press(" ", 0.05)

        time.sleep(0.5)

        press("w", 0.2)

        time.sleep(0.35)

        keyboard.release("d")

        time.sleep(0.5)

        if findImg("images/gui/cannon.png", 0.7):
            break

        loop += 1


def PepperVic():
    print("e")

    sendMessage("Searching pepper")

    print("ee")

    press("d", 2)

    keyboard.press("d")

    press(" ", 0.05)

    time.sleep(1.4)

    keyboard.release("d")

    time.sleep(0.05)

    keyboard.press("w")

    press(" ", 0.05)

    time.sleep(2)

    for _ in range(3):
        press(" ", 0.05)

        time.sleep(0.7)

    time.sleep(1)

    press(" ", 0.05)

    time.sleep(0.5)

    keyboard.release("w")

    time.sleep(0.05)

    press("w", "d", 2)

    press(" ", 0.05)

    press("d", 2.5)

    press("s", 0.5)

    ShiftLock()

    press("d", 0.2)

    for _ in range(9):
        keyboard.tap(Key.page_down)

        time.sleep(0.025)

    for _ in range(5):
        keyboard.tap(Key.page_up)

        time.sleep(0.025)

    for _ in range(4):
        keyboard.tap("o")

        time.sleep(0.15)


def PepperToCannon():
    sendMessage("Moving to cannon")
    press(Key.space, 0.1)
    keyboard.press("d")
    time.sleep(0.50)
    keyboard.release("d")
    time.sleep(0.10)
    keyboard.press("s")
    Waitspeed(15)
    keyboard.release("s")
    time.sleep(0.10)
    keyboard.press("w")
    Waitspeed(6.3)
    keyboard.release("w")
    time.sleep(0.10)
    keyboard.tap(",")
    keyboard.tap(",")
    keyboard.tap(",")
    press(Key.space, 0.1)
    time.sleep(0.1)
    press(Key.space, 0.1)
    time.sleep(2.62)
    keyboard.tap(".")
    time.sleep(0.87)
    press(Key.space, 0.1)
    time.sleep(1.25)


def MountVic():
    sendMessage("Checking mountian")
    keyboard.tap("e")
    time.sleep(1.70)
    press(Key.space, 0.1)
    press(Key.space, 0.1)
    time.sleep(1)
    keyboard.tap(",")
    keyboard.tap(",")
    time.sleep(0.38)

    press(Key.space, 0.1)
    time.sleep(1)

    keyboard.tap(".")
    keyboard.tap(".")
    keyboard.tap(".")
    keyboard.tap(".")

    press("s", 0.1)

    press("a", 0.5)

    keyboard.press("d")
    Waitspeed(6.9)

    press(" ", 0.1)

    Waitspeed(6.9)

    keyboard.release("d")
    time.sleep(0.10)
    keyboard.press("s")
    Waitspeed(2)
    keyboard.release("s")
    time.sleep(0.10)

    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    time.sleep(0.15)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(1)


def CactusVic():
    sendMessage("Checking cactus")
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    press(Key.space, 0.1)
    time.sleep(0.1)
    keyboard.press("d")
    keyboard.press("w")
    Waitspeed(29)
    keyboard.release("w")
    Waitspeed(13)
    keyboard.release("d")
    keyboard.press("w")
    Waitspeed(8)
    keyboard.release("w")
    time.sleep(0.05)
    keyboard.press("s")
    Waitspeed(3.6)
    keyboard.release("s")
    keyboard.tap(".")
    press(Key.space, 0.1)
    time.sleep(0.1)
    press(Key.space, 0.1)
    time.sleep(0.5)
    keyboard.tap(".")
    time.sleep(1.85)
    press(Key.space, 0.1)
    time.sleep(1.25)
    keyboard.press("d")
    Waitspeed(6.6)
    keyboard.release("d")
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(1)


def RoseVic():
    sendMessage("Checking rose")
    keyboard.press("w")
    Waitspeed(6)
    keyboard.press("a")
    Waitspeed(15)
    keyboard.release("w")
    Waitspeed(24)
    keyboard.release("a")
    press(Key.space, 0.1)
    time.sleep(0.1)
    keyboard.press("a")
    Waitspeed(4)
    keyboard.press("w")
    Waitspeed(17)
    keyboard.release("a")
    time.sleep(1)
    keyboard.press("w")
    Waitspeed(1.5)
    keyboard.release("w")
    time.sleep(0.10)
    keyboard.press("d")
    Waitspeed(10)
    keyboard.release("d")
    keyboard.tap(",")
    keyboard.tap(",")
    keyboard.press("d")
    Waitspeed(1)
    keyboard.release("d")
    time.sleep(0.50)
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("i")
    time.sleep(1)


def PepperMoveFromDetection():
    press(Key.space, 0.1)
    keyboard.press("d")
    time.sleep(0.50)
    keyboard.release("d")

    keyboard.press("d")
    Waitspeed(3.5)
    keyboard.release("d")

    keyboard.press("s")
    Waitspeed(7)
    keyboard.release("s")

    keyboard.press("w")
    Waitspeed(22)
    keyboard.release("w")

    keyboard.press("d")
    Waitspeed(6.5)
    keyboard.release("d")

    keyboard.press("s")
    Waitspeed(20)
    keyboard.release("s")

    keyboard.press("d")
    Waitspeed(6.5)
    keyboard.release("d")

    keyboard.press("w")
    Waitspeed(29.5)
    keyboard.release("w")

    keyboard.press("d")
    Waitspeed(7.5)
    keyboard.release("d")

    time.sleep(0.10)


def MountMoveFromDetection():
    press(Key.space, 0.1)
    time.sleep(0.1)
    keyboard.press("d")

    keyboard.press("d")
    Waitspeed(5.5)
    keyboard.release("d")

    keyboard.press("w")
    Waitspeed(8)
    keyboard.release("w")

    keyboard.press("d")
    Waitspeed(6.5)
    keyboard.release("d")

    keyboard.press("s")
    Waitspeed(11.5)
    keyboard.release("s")

    keyboard.press("a")
    Waitspeed(6.5)
    keyboard.release("a")

    keyboard.press("s")
    Waitspeed(4.5)
    keyboard.release("s")

    keyboard.press("d")
    Waitspeed(13)
    keyboard.release("d")

    keyboard.press("w")
    Waitspeed(25)
    keyboard.release("w")

    keyboard.press("d")
    Waitspeed(11.5)
    keyboard.release("d")


def CactusMoveFromDetection():
    keyboard.press("w")
    Waitspeed(6)
    keyboard.press("a")
    Waitspeed(15)
    keyboard.release("w")
    Waitspeed(24)
    keyboard.release("a")
    press(Key.space, 0.1)
    time.sleep(0.1)
    keyboard.press("w")
    Waitspeed(18)
    keyboard.release("w")

    keyboard.press("d")
    Waitspeed(30)
    keyboard.release("d")

    keyboard.press("s")
    Waitspeed(30)
    keyboard.release("s")

    press("w", 0.5)

    press("d", 0.75)

    press("w", 2.5)


def RoseMoveFromDetection():
    keyboard.press("a")
    Waitspeed(27)
    keyboard.release("a")

    press(Key.space, 0.1)
    time.sleep(0.1)
    keyboard.press("w")
    time.sleep(0.2)
    Waitspeed(10)
    keyboard.release("w")
    time.sleep(0.1)

    keyboard.press("d")
    Waitspeed(27)
    keyboard.release("d")

    time.sleep(0.1)
    keyboard.press("a")
    Waitspeed(6.5)
    keyboard.release("a")

    time.sleep(0.1)
    keyboard.press("w")
    Waitspeed(20)
    keyboard.release("w")

    time.sleep(0.1)
    keyboard.press("a")
    Waitspeed(5.5)
    keyboard.release("a")

    keyboard.press("s")
    Waitspeed(20)
    keyboard.release("s")

    time.sleep(0.1)
    keyboard.press("a")
    Waitspeed(4.5)
    keyboard.release("a")

    time.sleep(0.1)
    keyboard.press("w")
    Waitspeed(20)
    keyboard.release("w")

    time.sleep(0.1)
    keyboard.press("a")
    keyboard.press("w")
    Waitspeed(6.5)
    keyboard.release("a")
    keyboard.release("w")


def PepperKillCycle():
    start_time = time.time()
    timeout = 240  # 4 minutes in seconds

    while True:
        # Check if 4 minutes have passed
        if time.time() - start_time > timeout:
            print("4 minute timeout reached")
            return True

        # S movement
        for _ in range(10):
            keyboard.press("s")
            Waitspeed(2)
            keyboard.release("s")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # A movement
        for _ in range(5):
            keyboard.press("a")
            Waitspeed(2)
            keyboard.release("a")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # W movement
        for _ in range(10):
            keyboard.press("w")
            Waitspeed(2)
            keyboard.release("w")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # D movement
        for _ in range(6):
            keyboard.press("d")
            Waitspeed(2)
            keyboard.release("d")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False
        if detect_vic_defeat():
            sendScreenshot("Vic defeated, exiting cycle")
            return True


def MountKillCycle():
    start_time = time.time()
    timeout = 240  # 4 minutes in seconds

    while True:
        # Check if 4 minutes have passed
        if time.time() - start_time > timeout:
            print("4 minute timeout reached")
            return True

        # S movement
        for _ in range(10):
            keyboard.press("s")
            Waitspeed(2)
            keyboard.release("s")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # A movement
        for _ in range(3):
            keyboard.press("a")
            Waitspeed(2)
            keyboard.release("a")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # W movement
        for _ in range(10):
            keyboard.press("w")
            Waitspeed(2)
            keyboard.release("w")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # D movement
        for _ in range(4):
            keyboard.press("d")
            Waitspeed(2)
            keyboard.release("d")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False
        if detect_vic_defeat():
            sendScreenshot("Vic defeated, exiting cycle")
            return True


def CactusKillCycle():
    start_time = time.time()
    timeout = 240  # 4 minutes in seconds

    for _ in range(2):
        press(",", 0.1)

        time.sleep(0.1)

    press("w", 0.5)

    press("a", 1.5)

    while True:
        # Check if 4 minutes have passed
        if time.time() - start_time > timeout:
            print("4 minute timeout reached")
            return True

        # D movement
        for _ in range(6):
            keyboard.press("d")
            Waitspeed(2)
            keyboard.release("d")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        for _ in range(3):
            keyboard.press("s")

            Waitspeed(2)

            keyboard.release("s")

            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # A movement
        for _ in range(7):
            keyboard.press("a")
            Waitspeed(2)
            keyboard.release("a")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False
        if detect_vic_defeat():
            sendScreenshot("Vic defeated, exiting cycle")
            return True

        for _ in range(3):
            keyboard.press("w")

            Waitspeed(2)

            keyboard.release("w")

            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False


def RoseKillCycle():
    start_time = time.time()
    timeout = 240  # 4 minutes in seconds

    while True:
        # Check if 4 minutes have passed
        if time.time() - start_time > timeout:
            print("4 minute timeout reached")
            return True

        # S movement
        for _ in range(3):
            keyboard.press("s")
            Waitspeed(2)
            keyboard.release("s")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # A movement
        for _ in range(7):
            keyboard.press("a")
            Waitspeed(2)
            keyboard.release("a")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # W movement
        for _ in range(4):
            keyboard.press("w")
            Waitspeed(2)
            keyboard.release("w")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False

        # D movement
        for _ in range(8):
            keyboard.press("d")
            Waitspeed(2)
            keyboard.release("d")
            if detect_health_in_screenshot():
                print("Health detected, exiting cycle")
                return False
        if detect_vic_defeat():
            sendScreenshot("Vic defeated, exiting cycle")
            return True


def PepperRespawn():
    press("d", 2)

    keyboard.press("d")

    press(" ", 0.05)

    time.sleep(1.4)

    keyboard.release("d")

    time.sleep(0.05)

    keyboard.press("w")

    press(" ", 0.05)

    time.sleep(2)

    for _ in range(3):
        press(" ", 0.05)

        time.sleep(0.7)

    time.sleep(1)

    press(" ", 0.05)

    time.sleep(0.5)

    keyboard.release("w")

    time.sleep(0.05)

    press("w", "d", 2)

    press(" ", 0.05)

    press("d", 2.5)

    press("s", 0.5)

    press("d", 2)

    keyboard.press("d")

    press(" ", 0.05)

    time.sleep(1.4)

    keyboard.release("d")

    time.sleep(0.05)

    keyboard.press("w")

    press(" ", 0.05)

    time.sleep(2)

    for _ in range(3):
        press(" ", 0.05)

        time.sleep(0.7)

    time.sleep(1)

    press(" ", 0.05)

    time.sleep(0.5)

    keyboard.release("w")

    time.sleep(0.05)

    press("w", "d", 2)

    press(" ", 0.05)

    press("d", 2.5)

    press("s", 0.5)

    keyboard.press("d")
    press(" ", 0.05)
    time.sleep(0.5)
    keyboard.release("d")

    time.sleep(0.5)

    keyboard.press("w")
    keyboard.press("d")
    Waitspeed(25)
    keyboard.release("w")
    keyboard.release("d")


def MountRespawn():
    keyboard.tap("e")
    time.sleep(2)
    keyboard.press("w")
    Waitspeed(15)
    keyboard.release("w")
    time.sleep(0.025)
    keyboard.press("d")
    Waitspeed(15)
    keyboard.release("d")


def CactusRespawn():
    keyboard.tap("e")
    keyboard.press("s")
    keyboard.press("d")
    time.sleep(1)
    press(" ", 0.05)
    time.sleep(0.025)
    press(" ", 0.05)
    time.sleep(2)
    keyboard.release("s")
    keyboard.release("d")
    time.sleep(0.025)
    press(" ", 0.05)
    time.sleep(1.025)
    keyboard.press("s")
    Waitspeed(25)
    keyboard.release("s")
    time.sleep(0.025)
    keyboard.press("a")
    Waitspeed(10)
    keyboard.release("a")
    time.sleep(0.025)
    keyboard.press("w")
    Waitspeed(25)
    keyboard.release("w")
    time.sleep(0.025)


def RoseRespawn():
    keyboard.tap("e")
    keyboard.press("s")
    keyboard.press("d")
    time.sleep(0.1)
    press(" ", 0.05)
    time.sleep(0.025)
    press(" ", 0.05)
    time.sleep(2)
    keyboard.release("s")
    keyboard.release("d")
    time.sleep(0.025)
    press(" ", 0.05)
    time.sleep(1.025)
    keyboard.press("w")
    keyboard.press("d")
    Waitspeed(30)
    keyboard.release("w")
    Waitspeed(12)
    keyboard.release("d")
    time.sleep(0.025)


import threading


def timeout_checker(start_time, timeout=240):
    while True:
        if time.time() - start_time > timeout:
            print("4 minute timeout reached")
            return True

        time.sleep(1)


def PepperKillCycleLoop():
    start_time = time.time()
    timeout_thread = threading.Thread(target=timeout_checker, args=(start_time,))
    timeout_thread.daemon = True
    timeout_thread.start()

    while True:
        if not timeout_thread.is_alive():
            return True
        if PepperKillCycle():
            break
        Reset_char()
        WalkToRedCannon()
        PepperRespawn()


def MountKillCycleLoop():
    start_time = time.time()
    timeout_thread = threading.Thread(target=timeout_checker, args=(start_time,))
    timeout_thread.daemon = True
    timeout_thread.start()

    while True:
        if not timeout_thread.is_alive():
            return True
        if MountKillCycle():
            break
        Reset_char()
        WalkToRedCannon()


def CactusKillCycleLoop():
    start_time = time.time()
    timeout_thread = threading.Thread(target=timeout_checker, args=(start_time,))
    timeout_thread.daemon = True
    timeout_thread.start()

    while True:
        if not timeout_thread.is_alive():
            return True
        if CactusKillCycle():
            break
        Reset_char()
        WalkToRedCannon()


def RoseKillCycleLoop():
    start_time = time.time()
    timeout_thread = threading.Thread(target=timeout_checker, args=(start_time,))
    timeout_thread.daemon = True
    timeout_thread.start()

    while True:
        if not timeout_thread.is_alive():
            return True
        if RoseKillCycle():
            break
        Reset_char()
        WalkToRedCannon()


def KillVicBees():
    PepperVic()

    time.sleep(0.1)

    img = screenshot()

    if detectVicBee(img):
        vicBees = int(readFile(os.path.join(main_dir, "guiFiles", "currentHourVicBees.txt")))

        writeFile(os.path.join(main_dir, "guiFiles", "currentHourVicBees.txt"), str(vicBees + 1))

        sendScreenshot("Detected vic bee")
        for _ in range(2):
            time.sleep(0.1)
            keyboard.tap(Key.page_up)
        print("Vic detected, killing bees...")
        # kill pattern goes here
        PepperMoveFromDetection()
        PepperKillCycleLoop()
        return

    for _ in range(2):
        time.sleep(0.1)
        keyboard.tap(Key.page_up)
    PepperToCannon()
    MountVic()

    time.sleep(0.1)

    img = screenshot()

    if detectVicBee(img):
        sendScreenshot("Detected vic bee")
        for _ in range(2):
            time.sleep(0.1)
            keyboard.tap(Key.page_up)
        print("Vic detected, killing bees...")
        # kill pattern goes here
        MountMoveFromDetection()
        MountKillCycleLoop()
        return

    CactusVic()

    time.sleep(0.1)

    img = screenshot()

    if detectVicBee(img):
        sendScreenshot("Detected vic bee")
        time.sleep(0.1)
        for _ in range(2):
            time.sleep(0.1)
            keyboard.tap(Key.page_up)
            keyboard.tap(Key.page_up)
            keyboard.tap(Key.page_up)
            keyboard.tap(Key.page_up)
            keyboard.tap(Key.page_up)
            keyboard.tap(Key.page_up)
        print("Vic detected, killing bees...")
        # kill pattern goes here
        CactusMoveFromDetection()
        CactusKillCycleLoop()
        return
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)

    RoseVic()

    time.sleep(0.1)

    img = screenshot()

    if detectVicBee(img):
        sendScreenshot("Detected vic bee")
        time.sleep(0.1)
        keyboard.tap(Key.page_up)
        keyboard.tap(Key.page_up)
        keyboard.tap(Key.page_up)
        keyboard.tap(Key.page_up)
        keyboard.tap(Key.page_up)
        keyboard.tap(Key.page_up)
        keyboard.tap(".")
        keyboard.tap(".")
        print("Vic detected, killing bees...")
        # kill pattern goes here
        RoseMoveFromDetection()
        RoseKillCycleLoop()
        return


def canonToPepper(calibrate=False):
    press("d", 3)

    keyboard.press("d")

    press(" ", 0.05)

    time.sleep(1.4)

    keyboard.release("d")

    time.sleep(0.05)

    keyboard.press("w")

    press(" ", 0.05)

    time.sleep(2.5)

    for _ in range(3):
        press(" ", 0.05)

        time.sleep(0.7)

    time.sleep(1)

    press(" ", 0.05)

    time.sleep(0.85)

    keyboard.release("w")

    time.sleep(0.05)

    press("w", "d", 2)

    press(" ", 0.05)

    press("d", 2.5)

    press(" ", 0.05)

    press("d", 2.5)

    if calibrate:
        press("s", 2)

        press("d", 2)

        press("a", 0.5)

        press("w", 1)


def canonToMountain(calibrate=False):
    press("e", 0.05)

    time.sleep(3.5)


def canonToPineapple(calibrate=False):
    canonToMountain()

    press("a", 5.8)

    if calibrate:
        press("s", 2)

        press("a", 2)

        press("w", 0.5)

        press("w", 0.5)


def canonToCactus(calibrate=False):
    press("e", 0.05)

    time.sleep(0.8)

    for _ in range(2):
        press(" ", 0.05)

        time.sleep(0.1)

    press("s", "d", 2.5)

    press(" ", 0.05)

    time.sleep(1)

    press("a", 2)


def canonToPumpkin(calibrate=False):
    canonToCactus()

    press("d", 1)

    press("s", 3.5)

    if calibrate:
        press("s", 2)

        press("a", 2)

        press("w", 0.5)

        press("d", 0.5)


def canonToPine(calibrate=False):
    canonToPumpkin()

    press("d", 5)

    if calibrate:
        press("s", 2)

        press("d", 2)

        press("a", 0.5)

        press("w", 0.5)


def canonToStrawberry(calibrate=False):
    press("e", 0.05)

    time.sleep(0.75)

    for _ in range(2):
        press(" ", 0.1)

        time.sleep(0.1)

    press("d", 2)

    press(" ", 0.1)

    time.sleep(1)

    if calibrate:
        time.sleep(2)

        press("s", 2)

        press("d", 2)

        press("a", 0.5)

        press("w", 0.5)


def canonToSpider(calibrate=False):
    press("e", 0.05)

    time.sleep(0.75)

    for _ in range(3):
        press(" ", 0.1)

        time.sleep(0.1)

    time.sleep(1)

    press("w", 2)

    if calibrate:
        time.sleep(2)

        press("s", 2)

        press("d", 2)

        press("a", 0.5)

        press("w", 0.5)


def canonToBamboo(calibrate=False):
    press("e", 0.05)

    time.sleep(0.75)

    for _ in range(2):
        press(" ", 0.1)

        time.sleep(0.1)

    press("a", 2)

    press(" ", 0.1)

    time.sleep(1)

    press("s", 2)

    if calibrate:
        time.sleep(2)

        press("s", 2)

        press("a", 2)

        press("w", 0.5)

        press("d", 0.5)


def canonToClover(calibrate=False):
    press("e", 0.05)

    time.sleep(0.25)

    for _ in range(2):
        press(" ", 0.1)

        time.sleep(0.1)

    press("a", 5)


def canonToBlueFlower(calibrate=False):
    press("e", 0.05)

    time.sleep(0.2)

    for _ in range(2):
        press(" ", 0.1)

        time.sleep(0.1)

    press("a", 3)

    press(" ", 0.1)

    time.sleep(0.1)

    time.sleep(2)

    press("w", 2.5)

    press("d", 2.5)

def canonToSunflower(calibrate=False):
    press("a", 0.5)

    press("s", 5)

    if calibrate:
        press("d", 2)

        press("w", 3)

        press("s", 1)

        press("a", 0.5)

        press("w", 0.25)

def canonToDandelion(calibrate=False):
    canonToSunflower()

    press("a", 1.5)

    press(" ", 0.025)

    press("a", 4)

    press("w", 1)


def canonToMushroom(calibrate=False):
    canonToSunflower()

    press("a", 1.5)

    press(" ", 0.025)

    press("a", 3)

    press("s", 2)

    if calibrate:
        press("s", 2)

        press("a", 4)

        press("d", 0.5)

        press("w", 0.5)
