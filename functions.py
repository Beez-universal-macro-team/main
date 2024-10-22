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
import sys
import subprocess
from randomServer import joinRandomServer

main_dir = os.path.dirname(os.path.abspath(__file__))

mouse = mouseController()
keyboard = keyboardController()

walkSpeed = 33.35

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
    
        webhook.send(f"[{tm.hour}:{tm.minute}:{tm.second}] {message}") if picture == None else webhook.send(f"[{tm.hour}:{tm.minute}:{tm.second}] {message}", file=picture)

    except:
        pass


def sendScreenshot(message):
    screen = screenshot()

    screen.save("screenshot.png")

    screen = open("screenshot.png", "rb")

    t = threading.Thread(target=sendMessage, args=(message, discord.File(screen)))
    t.daemon = True

    t.start()

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

    time.sleep(args[len(args) - 1] * 33.35 / walkSpeed)

    for key in keys:
        keyboard.release(key)

        time.sleep(0.1)


def screenshot(monitor=False):
    with mss.mss() as sct:
        if monitor:
            screen = sct.grab(monitor)

        else:
            screen = sct.grab(sct.monitors[0])

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


#Paths and FUNCTIONS

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
                press('a', 2)  # Press 'w' for 1 second
            else:
                print("Maximum attempts reached. Image not found.")
                return False
            

def ClaimHive():
    press('d', 2)
    press('w', 24)
    press('w', 6)
    press('d', 6)
    press('a', 's', 4)

    while True:
        if MoveUntilHive():
            # Hive found, perform necessary actions
            break
        else:
            print("Retrying to find hive...")
            # You can add additional movements or actions here before retrying

    # Continue with the rest of the ClaimHive function

def WalkToCornerRamp():
    press('w', 6)
    press(((current_hive - 1) * 10) + 7, 'd')

def CornerToRedCannon():
    press(Key.space, 0.1)
    press('d', 0.20)
    press('w', 0.06)
    press('d', 7)

def WalkToRedCannon():
    for attempt in range(5):  # This will loop 5 times (0 to 4)
        WalkToCornerRamp()
        CornerToRedCannon()
        image_path = os.path.join(main_dir, 'images', 'gui', 'red_cannon.png')
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            return True  # Image found, exit the function
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            print(f"Attempt {attempt + 1} failed. Retrying...")
    
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
    max_diff = 30  # Adjust this value for color tolerance
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


def isColorClose(color1, color2, maxDiff):
    for index, col in enumerate(color1):
        if abs(col - color2[index]) > maxDiff:
            return False
    return True

def ClaimHiveWithRetries():
    max_retries = 4
    for attempt in range(max_retries):
        try:
            ClaimHive()
            print(f"Successfully claimed hive on attempt {attempt + 1}")
            return True  # Success, exit the function
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt < max_retries - 1:  # Don't reset on the last attempt
                print("Resetting and trying again...")
                Reset()
                time.sleep(8)  # Wait for reset to complete
            else:
                print("Max retries reached. Unable to claim hive.")
    return False  # All attempts failed


def ServerSetup():
    if not ClaimHiveWithRetries():
        print("Failed to claim hive after multiple attempts. Exiting MainLoop.")
        return False
    
def JoinServersUntilNight():
    while True:
        joinRandomServer()
        while True:
            if NightDetect():
                print("Night found!!")
                sendScreenshot("Night found!")
                if not ServerSetup():
                    print("ServerSetup failed. Exiting JoinServersUntilNight.")
                    return False
                time.sleep(1)
                return True
            else:
                print("Night not detected. Retrying...")
                sendScreenshot("Night not detected. Retrying...")
                leave()
                time.sleep(1)


