import subprocess
import platform
from functions import *

plat = platform.system().lower()

def moveMouseAhk(x, y):
    if plat == "windows":
        # Path to your AutoHotkey v2 executable
        ahk_path = r"C:\Program Files\AutoHotkey\v2\AutoHotkey64.exe"
        # Path to your AutoHotkey v2 script
        script_path = r"moveMouse.ahk"

        save_mouse_position(x, y, "coordinates.txt")

        # Run the script with x and y as parameters
        subprocess.run([ahk_path, script_path])

    else:
        clickXY(x, y)

def save_mouse_position(x, y, filename="coordinates.txt"):
    with open(filename, "w") as file:
        file.write(f"{x},{y}")