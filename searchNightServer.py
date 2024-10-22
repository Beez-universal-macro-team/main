from pynput.mouse import Button, Controller
import time
from randomServer import joinRandomServer
from functions import isWindowOpen, isColorClose, sendMessage, sendScreenshot, leave, reset, press, screenshot, click, offsetDims, findImg
import webbrowser

mouse = Controller()

claimHiveMonitor = {
        "top": offsetDims(62, "y"),
        "left": offsetDims(852, "x"),
        "width": offsetDims(1136 - 852, "x"),
        "height": offsetDims(121 - 62, "y"),
        "mon": 0,
}

def waitForLoading(maxWaitTime=20):
    tm = time.time()

    while True:
        screen = screenshot()

        if screen.getpixel(offsetDims((1300, 812), "list")) == (34, 87, 168):
            break

        elif time.time() - tm >= maxWaitTime:
            return False

        time.sleep(0.05)

    tm = time.time()

    while True:
        screen = screenshot()

        if screen.getpixel(offsetDims((1300, 812), "list")) != (34, 87, 168):
            return True

        elif time.time() - tm >= maxWaitTime:
            return False

        time.sleep(0.05)

def detectNight():
    screen = screenshot()

    if isColorClose(screen.getpixel(offsetDims((1376, 914), "list")), (86, 100, 107), 5):
        return True

    return False

def claimHive():
    press("w", "d", 4)

    time.sleep(0.1)

    press("s", 0.5)

    time.sleep(0.1)

    press("a", 0.3)

    claimingHive = True

    while claimingHive:
        hiveSlot = 7

        for loop in range(6):
            hiveSlot -= 1

            time.sleep(0.5)

            if findImg("images/claim_hive.png", 0.8):
                press("e", 0.5)

                sendScreenshot(f"Claimed hive slot {hiveSlot}")

                return hiveSlot

            elif loop == 5:
                break

            else:
                press("a", 1.1)

        reset(hive=False)

        press("w", "d", 4)

        time.sleep(0.025)

        press("s", 0.5)

        time.sleep(0.025)

        press("a", 0.3)

def findNightServer():
    hiveSlot = 0

    serverLoop = 0

    lastUrl = ""

    while True:
        serverLoop += 1

        if isWindowOpen("RobloxPlayerBeta.exe"):
            leave()

        if open("lastUrl.txt", "r").read() == lastUrl:
            joinRandomServer(1537690962)

        else:
            sendMessage("Joining alt...")

            webbrowser.open(open("lastUrl.txt", "r").read())

        lastUrl = open("lastUrl.txt", "r").read()

        if not waitForLoading(maxWaitTime=10):
            continue

        time.sleep(1)

        if not detectNight():
            continue

        sendScreenshot(f"Night server found :D (attempts: {serverLoop})")

        click(offsetDims((1000, 500), "list"))

        time.sleep(0.5)

        break
            
    return hiveSlot
