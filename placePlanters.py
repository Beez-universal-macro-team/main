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

def harvestPlanterInField(field):
    import paths

    sendMessage("Harvesting planter...")

    canon(rst=True)

    field = list(field.lower())

    field[0] = field[0].upper()

    field = "".join(field)

    globals()["canonTo" + field](calibrate=True)

    time.sleep(0.1)

    press("e", 0.05)

    time.sleep(0.5)

    screen = screenshot()
    screen.save("screenshot.png")

    time.sleep(0.1)

    pos = locateImageOnScreen3("screenshot.png", os.path.join(main_dir, "planters", "yesButton.png"), confidence=0.8)

    moveMouseAhk(pos[0] - 5, pos[1] - 5)
    moveMouseAhk(pos[0], pos[1])

    time.sleep(0.1)

    mouse.click()

    sendScreenshot("Harvested planter!")

def placePlanterInField(field, planter):
    import paths

    paths.sendMessage(f"Searching for {planter} planter")

    pos = paths.scrollTo(paths.os.path.join("planters", planter))

    if not pos:
        paths.sendMessage(f"Did not find {planter} planter... ;(")

        paths.time.sleep(0.5)

        paths.scrollUpInv()

        paths.time.sleep(0.1)

        return

    paths.sendMessage(f"Found {planter} planter! Placing it...")

    paths.canon(rst=True)

    field2 = list(field)
    field2[0] = field2[0].upper()
    field2 = "".join(field2)

    globals()["canonTo" + field2](calibrate=True)

    if pos != False:
        paths.moveMouseAhk(pos[0] - 5, pos[1] - 5)
        paths.moveMouseAhk(pos[0], pos[1])

        paths.pyautogui.dragTo(paths.screenDims[0] // 2, paths.screenDims[1] // 2)

    paths.time.sleep(0.5)

    screen = paths.screenshot()
    screen.save("screenshot.png")

    paths.time.sleep(0.1)

    pos = paths.locateImageOnScreen3("screenshot.png", paths.os.path.join(paths.main_dir, "planters", "yesButton.png"), confidence=0.8)

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
                if time.time() - float(plantersStatus[planter]["tmStarted"]) >= int(plantersStatus[planter]["tm"]) * 60:
                    planterDisp = "harvest"

                    plantersStatus[planter]["status"] = "harvest"

            if planterDisp == "free":
                placePlanterInField(plantersStatus[planter]["field"], getPlanterImgPath(plantersStatus[planter]["typ"]))

            else:
                harvestPlanterInField(plantersStatus[planter]["field"])

                time.sleep(1)

                placePlanterInField(plantersStatus[planter]["field"], getPlanterImgPath(plantersStatus[planter]["typ"]))

        plantersStatus[planter]["status"] = "growing"

        plantersStatus[planter]["tmStarted"] = str(time.time())

    writeFile(os.path.join("guiFiles", "plantersStatus.txt"), str(plantersStatus))