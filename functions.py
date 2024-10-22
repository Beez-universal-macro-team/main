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
