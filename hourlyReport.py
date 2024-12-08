import mouse
from functions import *
import easyocr
import keyboard
import matplotlib.pyplot as plt
from PIL import Image
import time

hourTime = 0

stingersHours = []
vicHours = []
hours = []

reader = easyocr.Reader(['en', 'es'])  # You can specify other languages as needed

time.sleep(1)

stingerBox = (
    30,
    650,
    95,
    680,
)


def getText(image_path):
    try:
        results = reader.readtext(image_path)

        return results[0][-2]

    except IndexError:
        return ""

    return txt


def getCurrentStingers():
    openInv()

    time.sleep(0.5)

    if findImg(os.path.join(main_dir, "images", "gui", "stinger.png"), 0.8):
        screen = screenshot()

        screen.save("screenshot.png")

        cropImg("screenshot.png", stingerBox)

        stingers = int(getText("screenshot.png"))

        openInv()

        return stingers

    openInv()

    return 0


def makeHourlyReportGraph():
    fig, ax1 = plt.subplots()

    # Plot for stingers
    ax1.set_xlabel('Hours')
    ax1.set_ylabel('Stingers', color='blue')
    ax1.plot(hours, stingersHours, color='blue', label='Stingers', marker='o')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Add data labels for stingers
    for x, y in zip(hours, stingersHours):
        ax1.text(x, y + 0.3, f'{y}', color='blue', fontsize=10, ha='center')

    # Create a second y-axis for vicious bees
    ax2 = ax1.twinx()
    ax2.set_ylabel('Vicious Bees', color='black')
    ax2.plot(hours, vicHours, color='black', label='Vicious Bees', marker='x')
    ax2.tick_params(axis='y', labelcolor='black')

    # Add data labels for vicious bees
    for x, y in zip(hours, vicHours):
        ax2.text(x, y + 0.1, f'{y}', color='black', fontsize=10, ha='center')

    # Add a title and grid
    plt.title('Hourly Report')
    plt.grid()

    time.sleep(0.1)

    plt.savefig('hourly.png')


def hourlyReport():
    global hourTime

    if time.time() - hourTime >= 60 * 60:
        hourTime = time.time()

        hours.append(len(hours) + 1)

        currentHourVicBees = int(readFile("currentHourVicBees.txt"))

        writeFile("currentHourVicBees.txt", "0")

        vicHours.append(currentHourVicBees)

        currentStingers = getCurrentStingers()

        stingersHours.append(currentStingers)

        makeHourlyReportGraph()

        screen = Image.open("hourly.png")

        sendImage("Hourly Report!", screen)
