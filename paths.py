from functions import *
import time

def PepperVic():
    sendMessage("Searching pepper")

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

    keyboard.press("d")
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
    Waitspeed(27)
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
    Waitspeed(35.5)
    keyboard.release("d")

    keyboard.press("s")
    Waitspeed(30)
    keyboard.release("s")

    keyboard.press("d")
    Waitspeed(6.5)
    keyboard.release("d")

    keyboard.press("w")
    Waitspeed(26)
    keyboard.release("w")

    keyboard.press("d")
    Waitspeed(4)
    keyboard.release("d")

    keyboard.press("s")
    Waitspeed(40)
    keyboard.release("s")

    keyboard.press("a")
    Waitspeed(6.5)
    keyboard.release("a")

    keyboard.press("w")
    keyboard.press("d")
    Waitspeed(6.5)
    keyboard.release("d")
    keyboard.release("w")


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


def PepperKillCycleLoop():
    while True:
        if PepperKillCycle():
            break
        Reset_char()
        WalkToRedCannon()

def MountKillCycleLoop():
    while True:
        if MountKillCycle():
            break
        Reset_char()
        WalkToRedCannon()

def CactusKillCycleLoop():
    while True:
        if CactusKillCycle():
            break
        Reset_char()
        WalkToRedCannon()

def RoseKillCycleLoop():
    while True:
        if RoseKillCycle():
            break
        Reset_char()
        WalkToRedCannon()

def KillVicBees():
    img = screenshot()
    
    PepperVic()
    if detectVicBee(img):
        sendScreenshot("Detected vic bee")
        for _ in range(2):
            time.sleep(0.1)
            keyboard.tap(Key.page_up)
        print("Vic detected, killing bees...")
        #kill pattern goes here
        PepperMoveFromDetection()
        PepperKillCycle()
        return 
    for _ in range(2):
        time.sleep(0.1)
        keyboard.tap(Key.page_up)
    PepperToCannon()
    MountVic()
    if detectVicBee(img):
        sendScreenshot("Detected vic bee")
        for _ in range(2):
            time.sleep(0.1)
            keyboard.tap(Key.page_up)
        print("Vic detected, killing bees...")
        #kill pattern goes here
        MountMoveFromDetection()
        MountKillCycle()
        return 
    CactusVic()
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
        #kill pattern goes here
        CactusMoveFromDetection()
        CactusKillCycle()
        return 
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    RoseVic()
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
        #kill pattern goes here
        RoseMoveFromDetection()
        RoseKillCycle()
        return 
