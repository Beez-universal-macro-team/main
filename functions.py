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
import requests
import random
import webbrowser
import time
import cv2
import numpy as np
from mss import mss
import imagehash

def mssScreenshot(x, y, w, h):
    with mss() as sct:
        monitor = {"top": y, "left": x, "width": w, "height": h}
        screen = sct.grab(monitor)
        return Image.frombytes("RGB", screen.size, screen.bgra, "raw", "BGRX")

def mssScreenshotNP(x, y, w, h):
    with mss() as sct:
        monitor = {"top": y, "left": x, "width": w, "height": h}
        return np.array(sct.grab(monitor))

def templateMatch(smallImg, bigImg):
    res = cv2.matchTemplate(bigImg, smallImg, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(res)

def locateImageOnScreen(target, x, y, w, h, threshold=0):
    screen = mssScreenshot(x, y, w, h)
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    _, max_val, _, max_loc = templateMatch(target, screen)
    if max_val < threshold:
        return None
    return (max_val, max_loc)

def locateTransparentImageOnScreen(target, x, y, w, h, threshold=0):
    screen = mssScreenshotNP(x, y, w, h)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2GRAY)
    target = cv2.cvtColor(target, cv2.COLOR_RGB2GRAY)
    _, max_val, _, max_loc = templateMatch(target, screen)
    if max_val < threshold:
        return None
    return (max_val, max_loc)

def similarHashes(hash1, hash2, threshold):
    return hash1-hash2 < threshold

def locateImageWithMaskOnScreen(image, mask, x, y, w, h, threshold=0):
    screen = mssScreenshotNP(x, y, w, h)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)
    res = cv2.matchTemplate(screen, image, cv2.TM_CCORR_NORMED, mask=mask)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    if max_val < threshold:
        return None
    return (max_val, max_loc)

def detect_image_beside(image_path, x_offset, y_offset, width, height, threshold=0.75):
    template = cv2.imread(os.path.join(main_dir, image_path))
    return locateTransparentImageOnScreen(template, x_offset, y_offset, width, height, threshold)


lastRequest = 0

servers_data = ""

psN = 0
psTime = 0

main_dir = os.path.dirname(os.path.abspath(__file__))

keyboard = keyboardController()

screenDims = pyautogui.size()

# Windows-specific imports and setup
if sys.platform == "win32":
    try:
        import pydirectinput as pag
        pag.PAUSE = 0.1
    except ImportError:
        pag = pyautogui

from pynput.mouse import Button, Controller
pynputMouse = Controller()

def teleport(x,y):
    pag.moveTo(int(x),int(y))

def moveTo(x,y, delay = 0.1):
    pag.moveTo(int(x),int(y), delay)
    pynputMouse.position = (int(x), int(y))

def mouseDown():
    pynputMouse.press(Button.left)
    if sys.platform == "win32":
        try:
            pag.mouseDown()
        except:
            pass

def mouseUp():
    pynputMouse.release(Button.left)
    if sys.platform == "win32":
        try:
            pag.mouseUp()
        except:
            pass

def moveBy(x = 0,y = 0):
    pag.move(x, y)  

def click():
    mouseDown()
    time.sleep(0.04)
    mouseUp()

def fastClick():
    pynputMouse.press(Button.left)
    pynputMouse.release(Button.left)

def readFile(fileName):
    if platform.system().lower() == "windows":
        while "/" in fileName:
            fileName = fileName.replace("/", "\\")

    full_path = os.path.join(main_dir, fileName)

    for _ in range(3):  # Try 3 times
        try:
            with open(full_path, "r") as file:
                content = file.read().strip()
                if content:
                    return content
                time.sleep(0.1)  # Brief pause between attempts
        except:
            time.sleep(0.1)
            
    return "0"  # Return "0" after 3 failed attempts



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

        print(message)

        webhook.send(f"[{tm.hour}:{tm.minute}:{tm.second}] {message}") if picture == None else webhook.send(
            f"[{tm.hour}:{tm.minute}:{tm.second}] {message}", file=picture)

    except:
        pass


def sendScreenshot(message):
    try:
        screen = screenshot()

        screen.save(os.path.join(main_dir, "images", "screenshot.png"))

        screen = open(os.path.join(main_dir, "images", "screenshot.png"), "rb")

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
        # Find primary monitor
        primary_monitor = None
        for monitor in sct.monitors[1:]:  # Skip the combined virtual monitor
            if monitor["left"] == 0 and monitor["top"] == 0:
                primary_monitor = monitor
                break

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

    # Clean the data by removing all spaces
    val_str = str(val).replace(" ", "")

    # Open the file in write mode, creating it if it doesn't exist
    with open(full_path, "w+") as file:
        file.write(val_str)

def joinRandomServer(place_id=1537690962):
    global lastRequest
    global servers_data
    global psN
    global psTime

    join = False

    if bool(readFile("guiFiles/joinPrivateServers.txt")):
        if time.time() - psTime >= 3:
            try:
                join_url = eval(readFile("guiFiles/privateServers.txt"))[psN]
                join_url = join_url.split("code=")[1]

                webbrowser.open("roblox://placeID=1537690962&linkcode=" + join_url)

                if psN >= 5:
                    psN = 1

                    psTime = time.time()

                else:
                    psN += 1

                return join_url

            except:
                if psN >= 5:
                    psN = 1

                    psTime = time.time()

                else:
                    psN += 1

                try:
                    url = joinRandomServer(place_id)

                except:
                    return ""

                return url

    if time.time() - lastRequest >= 30:
        # URL for Roblox game instances (servers)
        api_url = f'https://games.roblox.com/v1/games/{place_id}/servers/Public?sortOrder=Asc&limit=100'

        # Fetch the list of active servers
        response = requests.get(api_url)
        newServers_data = response.json()

        if 'data' in newServers_data and len(newServers_data['data']) > 0:
            servers_data = newServers_data

    try:
        if 'data' in servers_data and len(servers_data['data']) > 0:
            join = True

        else:
            time.sleep(10)

            url = joinRandomServer(place_id)

            return url

    except Exception as e:
        print(e)

    if join:
        servers = servers_data['data']

        # Choose a random server
        random_server = random.choice(servers)
        server_id = random_server['id']

        try:
            join_url = readFile("guiFiles/url.txt")

            if "roblox" in join_url:
                writeFile("guiFiles/url.txt", "")

            else:
                raise ValueError

            sendMessage("Joining alt...")

        except:
            # Generate the Roblox server join link
            join_url = f'roblox://placeID={place_id}&gameInstanceId={server_id}'

        # Open the Roblox client to join the server
        webbrowser.open(join_url)

        return join_url


def screenshot_area(x, y, width, height):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screen = sct.grab(monitor)
        screen = Image.frombytes("RGB", screen.size, screen.bgra, "raw", "BGRX")
        return screen


def getHoneyOffset():
    image_path = os.path.join(main_dir, 'images', 'gui', 'honey_OFFSETY.png')
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        return location.top - 7  # Returns Y coordinate 7 pixels above the found image
    except:
        return offsetDims(1000, "y")  # Default Y offset if image not found


def screenshot_health_area():
    honey_y = getHoneyOffset()
    screen_width = screenDims[0]

    # Calculate coordinates for right corner area
    x = offsetDims(1580, "x")  # Right side of screen
    y = honey_y  # Use honey position directly
    width = offsetDims(300, "x")  # Width of capture area
    height = offsetDims(200, "y")  # Height of capture area

    return screenshot_area(x, y, width, height)

# Paths and FUNCTIONS
print("loading vic bee AI...")
from AI.vic_detect import detectVicBee

print("Vic bee AI loaded, loading health AI...")
from AI.health_detect import detect_health_in_screenshot

print("Health AI loaded!")


def validateMoveSpeed():
    try:
        walkSpeed = int(readFile("guiFiles/moveSpeed.txt"))
        if walkSpeed < 10 or walkSpeed > 50:
            writeFile("guiFiles/moveSpeed.txt", "29")
            return 29
        return walkSpeed
    except:
        writeFile("guiFiles/moveSpeed.txt", "29")
        return 29


def Waitspeed(tm):
    walkSpeed = validateMoveSpeed()
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

    confidence = float(readFile("guiFiles/confidence.txt"))

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
                Waitspeed(9.05)
                keyboard.release("a")
                time.sleep(1)

            else:
                print("Maximum attempts reached. Image not found.")

                return False


def ClaimHive():
    keyboard.press("d")
    Waitspeed(4)
    keyboard.press("w")
    Waitspeed(20.75)
    keyboard.release("w")
    keyboard.release("d")
    time.sleep(0.05)
    keyboard.press("w")
    Waitspeed(4)
    keyboard.release("w")

    keyboard.press("w")
    Waitspeed(10)
    keyboard.release("w")

    keyboard.press("d")
    Waitspeed(8)
    keyboard.release("d")

    keyboard.press("a")
    keyboard.press("s")
    Waitspeed(5.5)
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
    Waitspeed(7)
    keyboard.release("w")
    time.sleep(0.1)
    keyboard.press("d")
    Waitspeed(((current_hive - 1) * 11) + 7)
    keyboard.release("d")


def CornerToRedCannon():
    press(Key.space, 0.1)
    keyboard.press("d")
    time.sleep(0.50)
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
            location = pyautogui.locateOnScreen(image_path, confidence=0.75)

            sendMessage("red cannon found")

            return True  # Image found, exit the function

        except pyautogui.ImageNotFoundException:
            time.sleep(1)

            print(f"Attempt {attempt + 1} failed. Retrying...")

            reset()

    sendMessage("Maximum attempts reached. Red cannon not found.")

    return False


def close_roblox():
    if sys.platform == "win32":
        subprocess.run(["taskkill", "/F", "/IM", "RobloxPlayerBeta.exe"], check=False)

    elif sys.platform == "darwin":
        subprocess.run(["pkill", "-9", "RobloxPlayer"], check=False)

    else:
        print("Unsupported operating system for closing Roblox")


def NightDetect():
    try:
        beesmas_enabled = int(readFile("guiFiles/beesmasToggle.txt"))
    except:
        beesmas_enabled = 0

    # Load model based on toggle
    if beesmas_enabled:
        target_color = (86, 100, 107)
    else:
        target_color = (24, 76, 28)

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


def detect_vic_defeat():
    keyboard.tap("/")
    time.sleep(0.25)
    keyboard.tap(Key.enter)
    time.sleep(0.25)

    image_path = os.path.join(main_dir, 'images', 'gui', 'defeated.png')
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.6)
        sendMessage("vic defeated")
        return True
    except:
        print("No vic defeat message detected")
        return False


def FloorDetect():
    target_color1 = (24, 76, 28)
    target_color2 = (24, 76, 28)
    max_diff = 30

    check_points = [
        offsetDims([1580, 921], "list"),
        offsetDims([510, 610], "list"),
        offsetDims([200, 200], "list"),
        offsetDims([1720, 200], "list"),
        offsetDims([960, 540], "list"),
        offsetDims([300, 800], "list"),
        offsetDims([1620, 800], "list"),
        offsetDims([800, 300], "list"),
        offsetDims([1120, 300], "list"),
        offsetDims([800, 780], "list"),
        offsetDims([1120, 780], "list"),
        offsetDims([960, 100], "list"),
        offsetDims([400, 400], "list"),
        offsetDims([1520, 400], "list"),
        offsetDims([400, 680], "list"),
        offsetDims([1520, 680], "list"),
        offsetDims([640, 540], "list"),
        offsetDims([1280, 540], "list"),
        offsetDims([960, 270], "list"),
        offsetDims([960, 810], "list"),
        offsetDims([200, 540], "list"),
        offsetDims([1720, 540], "list"),
        offsetDims([640, 100], "list"),
        offsetDims([1280, 980], "list")
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
            sendMessage("Max retries reached. Unable to claim hive.")

    return False  # All attempts failed


def activateRoblox():
    try:
        windows = pyautogui.getAllWindows()
        for window in windows:
            if 'Roblox' in window.title:
                window.maximize()
                window.activate()
                time.sleep(0.5)  # Give time for window operations
                print("Roblox window activated and maximized.")
                return True
        return False
    except:
        return False


def DetectLoading(timeout):
    target_color = (34, 87, 168)  # RGB equivalent of 0x2257A8
    start_time = time.time()
    window_activated = False

    # Wait for loading color to appear
    while True:
        if not window_activated:
            window_activated = activateRoblox()
        pixel_color = pyautogui.pixel(458, 151)

        if isColorClose(pixel_color, target_color, 10):
            print("Loading color detected!")
            break

        if time.time() - start_time >= timeout:
            return False

        time.sleep(1)  # Increased to 1 second

    # Wait for loading color to disappear with timeout
    start_time = time.time()  # Reset timer for disappearance check

    while True:
        if not window_activated:
            window_activated = activateRoblox()
        pixel_color = pyautogui.pixel(458, 151)

        if not isColorClose(pixel_color, target_color, 10):
            print("Loading complete!")
            time.sleep(2)
            break

        if time.time() - start_time >= timeout:
            print("restricted experience")
            close_roblox()
            return False

        time.sleep(1)  # Increased to 1 second

    return True


def ServerSetup():
    if not ClaimHiveWithRetries():
        print("Failed to claim hive after multiple attempts. Exiting MainLoop.")
        return False
    sendMessage("Claimed hive")
    WalkToRedCannon()
    sendMessage("Moved to cannon")
    return True


def ShiftLock():
    keyboard.press(Key.shift)
    time.sleep(0.1)  # Increased delay
    keyboard.release(Key.shift)
    print("Shift lock released")
    time.sleep(0.5)  # Wait to confirm state change
    return True


def JoinServersUntilNight():
    while True:
        joinRandomServer()
        sendMessage("searching for night")

        if not DetectLoading(int(readFile("guiFiles/maxLoadTime.txt"))):
            print("Loading timed out, trying new server...")
            close_roblox()
            continue  # Goes back to joinRandomServer()

        while True:
            if NightDetect():
                sendScreenshot("Night found!")

                if not ServerSetup():
                    print("ServerSetup failed. Exiting JoinServersUntilNight.")

                    break

                KillVicBees()

                time.sleep(1)

                break  # Breaks inner while loop to go back to joinRandomServer()
            else:
                print("Night not detected. Retrying...")

                # sendScreenshot("Night not detected. Retrying...") lowering screenshot send rate

                leave()

                time.sleep(2)

                break  # Breaks inner while loop to go back to joinRandomServer()


from paths import *


def MainLoopMacro():
    # PepperKillCycle()
    # KillVicBees()
    JoinServersUntilNight()

