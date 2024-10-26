from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Controller as keyboardController, Key
import time
from PIL import Image, ImageGrab
import mss
import discord
import psutil
import threading
import pyautogui
from datetime import datetime
import platform
import os

main_dir = os.path.dirname(os.path.abspath(__file__))

mouse = mouseController()
keyboard = keyboardController()

screenDims = pyautogui.size()

def isColorClose(color1, color2, maxDiff):
    for index, col in enumerate(color1):
        if abs(col - color2[index]) <= maxDiff:
            continue

        else:
            return False

    return True


def isWindowOpen(windowName):
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] == windowName:
                return True

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False


def sendMessage(message, picture=None):
    try:
        webhook = discord.SyncWebhook.from_url(readFile("guiFiles/webhook.txt"))

        tm = datetime.now()

        webhook.send(f"[{tm.hour}:{tm.minute}:{tm.second}] {message}") if picture == None else webhook.send(
            f"[{tm.hour}:{tm.minute}:{tm.second}] {message}", file=picture)

    except:
        pass


def sendScreenshot(message):
    try:
        screen = screenshot()

        screen.save("screenshot.png")

        screen = open("Images/screenshot.png", "rb")

        t = threading.Thread(target=sendMessage, args=(message, discord.File(screen)))
        t.daemon = True

        t.start()

    except:
        pass


def leave():
    keyboard.tap(Key.esc)

    time.sleep(0.025)

    keyboard.tap("l")

    time.sleep(0.025)

    keyboard.tap(Key.enter)


def reset(hive=True):
    press(Key.esc, 0.05)

    time.sleep(0.05)

    press("r", 0.05)

    time.sleep(0.05)

    press(Key.enter, 0.05)

    time.sleep(8)

    if hive:
        if not findImg("images/make_honey1.png", 0.7) and not findImg("images/make_honey2.png", 0.7):
            press("w", "d", 3)


def findImg(img, confidence):
    try:
        pos = pyautogui.locateCenterOnScreen(img, confidence=confidence)

        pyautogui.moveTo(pos)

        return True

    except:
        return False


def press(*args):
    keys = list(args)
    keys.pop(len(keys) - 1)

    for key in keys:
        keyboard.press(key)

        time.sleep(0.1)

    walkSpeed = float(readFile("guiFiles/moveSpeed.txt"))

    time.sleep(args[len(args) - 1] * 33.35 / walkSpeed)

    for key in keys:
        keyboard.release(key)

        time.sleep(0.1)


def screenshot(monitor=False):
    with mss.mss() as sct:
        # Get primary monitor
        primary_monitor = sct.monitors[1]  # Monitor 1 is typically the primary display

        screen = sct.grab(primary_monitor)

    screen = Image.frombytes("RGB", screen.size, screen.bgra, "raw", "BGRX")
    return screen


def click(pos):
    mouse.position = pos

    time.sleep(0.05)

    mouse.click(Button.left)

    time.sleep(0.05)


def offsetDims(pos, xy):
    if xy == "list":
        return (int(pos[0] * (screenDims[0] / 1920)), int(pos[1] * (screenDims[1] / 1080)))

    elif xy == "x":
        return int(pos * (screenDims[0] / 1920))

    else:
        return int(pos * (screenDims[1] / 1080))


def writeFile(fileName, val):
    if platform.system().lower() == "windows":
        while "/" in fileName:
            fileName = fileName.replace("/", "\\")

    full_path = os.path.join(main_dir, fileName)

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Open the file in write mode, creating it if it doesn't exist
    with open(full_path, "w+") as file:
        file.write(str(val))


def readFile(fileName):
    if platform.system().lower() == "windows":
        while "/" in fileName:
            fileName = fileName.replace("/", "\\")

    full_path = os.path.join(main_dir, fileName)

    with open(full_path, "r") as file:
        return file.read()


# Paths and FUNCTIONS

import sys
import subprocess
from randomServer import joinRandomServer
from AI.vic_detect import detect_vic_in_screenshot


def Waitspeed(tm):
    try:
        walkSpeed = int(readFile("guiFiles/moveSpeed.txt"))
    except:
        walkSpeed = 33.35  # Default value if file is empty or invalid
    
    time.sleep((tm * 4) / walkSpeed)



def Reset():
    keyboard.tap(Key.esc)

    time.sleep(0.025)

    keyboard.tap("r")

    time.sleep(0.025)

    keyboard.tap(Key.enter)

    time.sleep(7)


def MoveUntilHive():
    global current_hive

    image_path = os.path.join(main_dir, 'images', 'gui', 'claimhive.png')

    confidence = 0.8

    for attempt in range(1, 6):  # Loop 5 times, from 1 to 5
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)

            keyboard.tap("e")

            current_hive = attempt  # Update the current hive number

            time.sleep(1)

            return True  # Image found

        except pyautogui.ImageNotFoundException:
            if attempt < 5:
                keyboard.press("a")
                Waitspeed(11)
                keyboard.release("a")

            else:
                print("Maximum attempts reached. Image not found.")

                return False


def ClaimHive():
    keyboard.press("d")
    Waitspeed(4)
    keyboard.press("w")
    Waitspeed(25)
    keyboard.release("w")
    keyboard.release("d")

    keyboard.press("w")
    Waitspeed(8)
    keyboard.release("w")

    keyboard.press("d")
    Waitspeed(8)
    keyboard.release("d")

    keyboard.press("a")
    keyboard.press("s")
    Waitspeed(7.6)
    keyboard.release("a")
    keyboard.release("s")


    if MoveUntilHive():
        return True

    else:
        print("Retrying to find hive...")
        return False

    # Continue with the rest of the ClaimHive function


def WalkToCornerRamp():
    keyboard.press("w")
    Waitspeed(4)
    keyboard.release("w")
    time.sleep(0.1)
    keyboard.press("d")
    Waitspeed(((current_hive - 1) * 11) + 7)
    keyboard.release("d")



def CornerToRedCannon():
    press(Key.space, 0.1)
    keyboard.press("d")
    time.sleep(0.10)
    keyboard.release("d")
    time.sleep(0.50)
    keyboard.press("w")
    Waitspeed(0.5)
    keyboard.release("w")
    keyboard.press("d")
    Waitspeed(7.5)
    keyboard.release("d")


def WalkToRedCannon():
    for attempt in range(5):  # This will loop 5 times (0 to 4)
        WalkToCornerRamp()
        CornerToRedCannon()

        image_path = os.path.join(main_dir, 'images', 'gui', 'red_cannon.png')

        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            print("Red cannon found!")

            return True  # Image found, exit the function

        except pyautogui.ImageNotFoundException:
            time.sleep(1)

            print(f"Attempt {attempt + 1} failed. Retrying...")

            reset()

    print("Maximum attempts reached. Red cannon not found.")

    return False


def close_roblox():
    if sys.platform == "win32":
        subprocess.run(["taskkill", "/F", "/IM", "RobloxPlayerBeta.exe"], check=False)

    elif sys.platform == "darwin":
        subprocess.run(["pkill", "-9", "RobloxPlayer"], check=False)

    else:
        print("Unsupported operating system for closing Roblox")


def NightDetect():
    target_color = (86, 100, 107)

    max_diff = 10  # Adjust this value for color tolerance

    screen_width, screen_height = pyautogui.size()

    # Check multiple points on the screen for better accuracy
    check_points = [
        (screen_width // 2, screen_height // 2),
        (screen_width // 4, screen_height // 4),
        (3 * screen_width // 4, 3 * screen_height // 4)
    ]

    for point in check_points:
        pixel_color = pyautogui.pixel(point[0], point[1])

        if isColorClose(pixel_color, target_color, max_diff):
            print(f"Night detected at point {point}!")

            return True

    print("Night not detected.")

    return False


def FloorDetect():
    target_color1 = (37, 150, 190)
    target_color2 = (88, 100, 108)

    max_diff = 30 # Adjust this value for color tolerance

    screen_width, screen_height = pyautogui.size()

    # Calculate the check points based on screen dimensions
    check_points = [
        (int(1580 * screen_width / 1920), int(921 * screen_height / 1080)),
        (int(510 * screen_width / 1920), int(610 * screen_height / 1080)),
        (int(200 * screen_width / 1920), int(200 * screen_height / 1080)),
        (int(1720 * screen_width / 1920), int(200 * screen_height / 1080)),
        (int(960 * screen_width / 1920), int(540 * screen_height / 1080)),
        (int(300 * screen_width / 1920), int(800 * screen_height / 1080)),
        (int(1620 * screen_width / 1920), int(800 * screen_height / 1080)),
        (int(800 * screen_width / 1920), int(300 * screen_height / 1080)),
        (int(1120 * screen_width / 1920), int(300 * screen_height / 1080)),
        (int(800 * screen_width / 1920), int(780 * screen_height / 1080)),
        (int(1120 * screen_width / 1920), int(780 * screen_height / 1080)),
        (int(960 * screen_width / 1920), int(100 * screen_height / 1080)),
        (int(400 * screen_width / 1920), int(400 * screen_height / 1080)),
        (int(1520 * screen_width / 1920), int(400 * screen_height / 1080)),
        (int(400 * screen_width / 1920), int(680 * screen_height / 1080)),
        (int(1520 * screen_width / 1920), int(680 * screen_height / 1080)),
        (int(640 * screen_width / 1920), int(540 * screen_height / 1080)),
        (int(1280 * screen_width / 1920), int(540 * screen_height / 1080)),
        (int(960 * screen_width / 1920), int(270 * screen_height / 1080)),
        (int(960 * screen_width / 1920), int(810 * screen_height / 1080)),
        (int(200 * screen_width / 1920), int(540 * screen_height / 1080)),
        (int(1720 * screen_width / 1920), int(540 * screen_height / 1080)),
        (int(640 * screen_width / 1920), int(100 * screen_height / 1080)),
        (int(1280 * screen_width / 1920), int(980 * screen_height / 1080))
    ]

    for point in check_points:
        pixel_color = pyautogui.pixel(point[0], point[1])

        if isColorClose(pixel_color, target_color1, max_diff) or isColorClose(pixel_color, target_color2, max_diff):
            print(f"Floor detected at point {point}!")

            return True

    print("Floor not detected.")

    return False


def Reset_char():
    Reset()

    if FloorDetect():
        print("Floor detected.")

    else:
        print("Floor not detected. Rotating...")
        for _ in range(4):
            press('.', 0.1)


def ClaimHiveWithRetries():
    max_retries = 4
    for attempt in range(max_retries):
        if attempt > 0:  # Only reset after first attempt
            Reset()
            
        if ClaimHive():
            print(f"Successfully claimed hive on attempt {attempt + 1}")
            return True  # Success, exit the function
        
        print(f"Attempt {attempt + 1} failed to claim hive")
        if attempt == max_retries - 1:  # Last attempt
            print("Max retries reached. Unable to claim hive.")
            
    return False  # All attempts failed




def DetectLoading(timeout):
    target_color = (34, 87, 168)  # RGB equivalent of 0x2257A8

    start_time = time.time()

    # Wait for loading color to appear
    while True:
        pixel_color = pyautogui.pixel(458, 151)

        if isColorClose(pixel_color, target_color, 10):
            print("Loading color detected!")

            break

        if time.time() - start_time >= timeout:
            return False

        time.sleep(0.1)

    # Wait for loading color to disappear with timeout
    start_time = time.time()  # Reset timer for disappearance check

    while True:
        pixel_color = pyautogui.pixel(458, 151)

        if not isColorClose(pixel_color, target_color, 10):
            print("Loading complete!")

            time.sleep(2)

            break

        if time.time() - start_time >= timeout:
            print("restricted experience")

            close_roblox()

            return False

        time.sleep(0.1)

    return True


def ServerSetup():
    if not ClaimHiveWithRetries():
        print("Failed to claim hive after multiple attempts. Exiting MainLoop.")
        return False
    return True


def ShiftLock():
    keyboard.press(Key.shift)
    time.sleep(0.1)  # Increased delay
    keyboard.release(Key.shift)
    print("Shift lock released")
    time.sleep(0.5)  # Wait to confirm state change
    return True





def PepperVic():
    keyboard.press("d")
    Waitspeed(24)
    keyboard.release("d")
    press(Key.space, 0.1)
    keyboard.press("d")
    time.sleep(0.10)
    keyboard.release("d")
    time.sleep(0.50)
    keyboard.press("w")
    Waitspeed(7)
    keyboard.release("w")
    time.sleep(0.10)
    press(Key.space, 0.1)
    keyboard.press("w")
    time.sleep(0.65)
    Waitspeed(10)
    keyboard.release("w")
    time.sleep(0.10)
    keyboard.press("d")
    Waitspeed(5)
    keyboard.release("d")
    time.sleep(0.10)
    keyboard.press("w")
    press(Key.space, 0.1)
    time.sleep(0.50)
    press(Key.space, 0.1)
    press(Key.space, 0.1)
    keyboard.release("w")
    time.sleep(0.50)
    keyboard.press("w")
    Waitspeed(15)
    keyboard.release("w")
    time.sleep(0.1)
    press(Key.space, 0.1)
    keyboard.press("w")
    time.sleep(0.65)
    keyboard.release("w")
    time.sleep(0.10)
    keyboard.press("w")
    keyboard.press("d")
    Waitspeed(17)
    keyboard.release("w")
    keyboard.release("d")
    time.sleep(0.10)
    press(Key.space, 0.1)
    keyboard.press("d")
    time.sleep(0.50)
    keyboard.release("d")
    time.sleep(0.10)
    keyboard.press("d")
    Waitspeed(18)
    keyboard.release("d")
    time.sleep(0.10)
    keyboard.press("s")
    Waitspeed(2)
    keyboard.release("s")
    ShiftLock()
    keyboard.tap(Key.page_down) 
    keyboard.tap(Key.page_down) 
    keyboard.tap("o")
    keyboard.tap("o")
    keyboard.tap("o")
    
def PepperToCannon():
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
    Waitspeed(5.8)
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
    time.sleep(0.70)
    press(Key.space, 0.1)
    time.sleep(1.25)

def MountVic():
    keyboard.tap("e")
    time.sleep(2.05)
    press(Key.space, 0.1)
    press(Key.space, 0.1)
    time.sleep(2)
    keyboard.press("w")
    Waitspeed(7.5)
    keyboard.release("w")
    time.sleep(0.10)
    keyboard.press("s")
    Waitspeed(3.5)
    keyboard.release("s")
    keyboard.tap(".")
    keyboard.tap(".")
    keyboard.tap(Key.page_down) 
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down) 
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down) 
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down) 
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    time.sleep(0.10)
    keyboard.tap("o")
    keyboard.tap("o")
    keyboard.tap("o")

def CactusVic():
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
    Waitspeed(6.5)
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
    time.sleep(1.70)
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




def KillVicBees():
    PepperVic()
    if detect_vic_in_screenshot():
        for _ in range(2):
            time.sleep(0.1)
            keyboard.tap(Key.page_up)
        print("Vic detected, killing bees...")
        #kill pattern goes here
        return 
    for _ in range(2):
        time.sleep(0.1)
        keyboard.tap(Key.page_up)
    PepperToCannon()
    MountVic()
    if detect_vic_in_screenshot():
        for _ in range(2):
            time.sleep(0.1)
            keyboard.tap(Key.page_up)
        print("Vic detected, killing bees...")
        #kill pattern goes here
        return 
    CactusVic()
    if detect_vic_in_screenshot():
        for _ in range(2):
            time.sleep(0.1)
            keyboard.tap(Key.page_up)
        print("Vic detected, killing bees...")
        #kill pattern goes here
        return 
    



def JoinServersUntilNight():
    while True:
        joinRandomServer()

        if not DetectLoading(int(readFile("guiFiles/maxLoadTime.txt"))):
            print("Loading timed out, trying new server...")
            close_roblox()
            continue  # Goes back to joinRandomServer()

        while True:
            if NightDetect():
                print("Night found!!")

                sendScreenshot("Night found!")

                if not ServerSetup():
                    print("ServerSetup failed. Exiting JoinServersUntilNight.")

                    break

                KillVicBees()

                time.sleep(1)

                return True
            else:
                print("Night not detected. Retrying...")

                #sendScreenshot("Night not detected. Retrying...") lowering screenshot send rate

                leave()

                time.sleep(2)

                break  # Breaks inner while loop to go back to joinRandomServer()


def MainLoopMacro():
    #CactusVic()
    #KillVicBees()
    JoinServersUntilNight()
