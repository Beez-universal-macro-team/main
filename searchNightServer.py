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

        if isColorClose(screen.getpixel(offsetDims((1300, 812), "list")), (34, 87, 168), 3):
            break

        elif time.time() - tm >= maxWaitTime:
            return False

        time.sleep(0.05)

    tm = time.time()

    while True:
        screen = screenshot()

        if not isColorClose(screen.getpixel(offsetDims((1300, 812), "list")), (34, 87, 168), 3):
            return True

        elif time.time() - tm >= maxWaitTime:
            return False

        time.sleep(0.05)

def detectNight():
    screen = screenshot()

    if isColorClose(screen.getpixel(offsetDims((1376, 914), "list")), (86, 100, 107), 5):
        return True

    return False

def findNightServer(maxWaitTime=10, alt=False):
    hiveSlot = 0

    serverLoop = 0

    lastUrl = ""

    while True:
        serverLoop += 1

        if isWindowOpen("RobloxPlayerBeta.exe"):
            leave()

        if not alt:
            if open("lastUrl.txt", "r").read() == lastUrl:
                joinRandomServer(1537690962)

            else:
                sendMessage("Joining alt...")

                webbrowser.open(open("lastUrl.txt", "r").read())

        else:
            url = joinRandomServer(1537690962)

        lastUrl = open("lastUrl.txt", "r").read()

        if not waitForLoading(maxWaitTime=maxWaitTime):
            continue

        click(offsetDims((1000, 500), "list"))

        time.sleep(1)

        if not detectNight():
            continue

        sendScreenshot(f"Night server found :D (attempts: {serverLoop})")

        click(offsetDims((1000, 500), "list"))

        time.sleep(0.5)

    return url