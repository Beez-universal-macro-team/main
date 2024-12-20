from functions import *
from paths import *


def getPlanterImgPath(planter):
    if planter == "BlueClay":
        return "blueClay"

    elif planter == "RedClay":
        return "redClay"

    elif planter == "Candy":
        return "candy"

    elif planter == "HeatTreated":
        return "heatTreated"

    elif planter == "Hydroponic":
        return "hydroponic"

    elif planter == "Pesticide":
        return "pesticide"

    elif planter == "Plastic":
        return "plastic"

    elif planter == "Tacky":
        return "tacky"

    elif planter == "Pop":
        return "pop"


def harvestPlanterInField(field, tries=0):
    try:
        sendMessage("Harvesting planter...")

        canon(rst=True)

        field = list(field)

        field[0] = field[0].upper()

        field = "".join(field)

        print("going to field")

        globals()["canonTo" + field](calibrate=True)

        time.sleep(0.1)

        press("e", 0.05)

        time.sleep(0.5)

        screen = screenshot()
        screen.save("screenshot.png")

        time.sleep(0.1)

        pos = locateImageOnScreen3("screenshot.png", os.path.join(main_dir, "planters", "yesButton.png"),
                                   confidence=0.8)

        if pos != False:
            moveMouseAhk(pos[0] - 5, pos[1] - 5)
            moveMouseAhk(pos[0], pos[1])

            time.sleep(0.1)

            mouse.click()

            sendScreenshot("Harvested planter!")

        else:
            harvestPlanterInField(field, tries=tries + 1)

    except Exception as e:
        print(e)

        if tries < 3:
            harvestPlanterInField(field, tries=tries + 1)


def placePlanterInField(field, planter, harvest=False):
    import paths

    paths.sendMessage(f"Searching for {planter} planter")

    pos = paths.scrollTo(paths.os.path.join("planters", planter))

    if not pos:
        paths.sendMessage(f"Did not find {planter} planter... ;(")

        paths.time.sleep(0.5)

        paths.scrollUpInv()

        paths.time.sleep(0.1)

        return False

    paths.sendMessage(f"Found {planter} planter! Placing it...")

    if not harvest:
        paths.canon(rst=True)

        field2 = list(field)
        field2[0] = field2[0].upper()
        field2 = "".join(field2)

        globals()["canonTo" + field2](calibrate=True)

    if pos != False:
        paths.moveMouseAhk(pos[0] - 5, pos[1] - 5)
        paths.moveMouseAhk(pos[0], pos[1])

        paths.pyautogui.dragTo(paths.screenDims[0] // 2, paths.screenDims[1] // 2)

    else:
        placePlanterInField(field, planter)

        return

    paths.time.sleep(0.5)

    screen = paths.screenshot()
    screen.save("screenshot.png")

    paths.time.sleep(0.1)

    pos = paths.locateImageOnScreen3("screenshot.png", paths.os.path.join(paths.main_dir, "planters", "yesButton.png"),
                                     confidence=0.8)

    paths.moveMouseAhk(pos[0] - 5, pos[1] - 5)
    paths.moveMouseAhk(pos[0], pos[1])

    paths.time.sleep(0.1)

    paths.mouse.click()

    paths.time.sleep(0.5)

    paths.scrollUpInv()

    paths.sendScreenshot(f"Placed {planter} planter!")


def plantersLogic():
    plantersStatus = eval(readFile(os.path.join("guiFiles", "plantersStatus.txt")))

    for planter in plantersStatus.keys():
        if plantersStatus[planter]["enabled"] == "1":
            planterDisp = plantersStatus[planter]["status"]

            if planterDisp == "growing":
                sendMessage(f"Time left before harvesting planters: {max(0, round(int(plantersStatus[planter]["tm"]) - (time.time() - float(plantersStatus[planter]["tmStarted"])) / 60))} minutes")

                if time.time() - float(plantersStatus[planter]["tmStarted"]) >= int(plantersStatus[planter]["tm"]) * 60:
                    planterDisp = "harvest"

                    plantersStatus[planter]["status"] = "harvest"

            if planterDisp == "free":
                res = placePlanterInField(plantersStatus[planter]["field"],
                                          getPlanterImgPath(plantersStatus[planter]["typ"]))

                if res == False:
                    harvestPlanterInField(plantersStatus[planter]["field"])

                    time.sleep(1)

                    placePlanterInField(plantersStatus[planter]["field"], getPlanterImgPath(plantersStatus[planter]["typ"]), harvest=True)

                plantersStatus[planter]["status"] = "growing"

                plantersStatus[planter]["tmStarted"] = str(time.time())

                writeFile(os.path.join("guiFiles", "plantersStatus.txt"), str(plantersStatus))

            if planterDisp == "harvest":
                harvestPlanterInField(plantersStatus[planter]["field"])

                time.sleep(1)

                placePlanterInField(plantersStatus[planter]["field"], getPlanterImgPath(plantersStatus[planter]["typ"]), harvest=True)

                plantersStatus[planter]["status"] = "growing"

                plantersStatus[planter]["tmStarted"] = str(time.time())

                writeFile(os.path.join("guiFiles", "plantersStatus.txt"), str(plantersStatus))

            writeFile(os.path.join("guiFiles", "plantersStatus.txt"), str(plantersStatus))

    writeFile(os.path.join("guiFiles", "plantersStatus.txt"), str(plantersStatus))
