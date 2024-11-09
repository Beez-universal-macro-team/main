import subprocess
import sys

required_libraries = [
    'pynput',
    'Pillow',
    'mss',
    'discord.py',
    'discord',
    'psutil',
    'customtkinter',
    'requests',
    'fonttools',    
    'ultralytics',
    'matplotlib',
    'opencv-python',  # For image processing
    'numpy',  # For array operations
    'colorama',  # Added colorama
    'ImageHash'  # Added ImageHash for image comparison
]


def install(*packages):
    subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])

# First try to install pyautogui separately with special flags
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "--user", "pyautogui"])
    print("'pyautogui' installed successfully.")
except subprocess.CalledProcessError:
    print("Failed to install 'pyautogui'.")

# Then continue with the rest of the installations
try:
    install("pip", "--upgrade")
    install("setuptools", "--upgrade")
    print("Pip upgraded successfully.")
except subprocess.CalledProcessError:
    print("Failed to upgrade pip.")

# Install remaining libraries
for lib in required_libraries:
    try:
        install(lib)
        print(f"'{lib}' installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install '{lib}'.")

from colorama import init, Fore
init()  # Initialize colorama

print(Fore.GREEN + "All libraries installed (if available).")
print(Fore.YELLOW + "If main.py has issues starting, run this again and check for errors and DM a dev")
print(Fore.CYAN + "Press Enter to close..." + Fore.RESET)
input()


