import subprocess
import sys

# List of required libraries
required_libraries = [
    'pyautogui',
    'pynput',
    'Pillow',  # for PIL
    'mss',
    'discord.py',  # for discord
    'discord',
    'psutil',
    'customtkinter',
    'requests',
    'fonttools',  # for fontTools.misc.textTools
    'numpy==1.26.2',
    'ultralytics',
    'matplotlib',
    'audioop-lts'
]

# Function to install libraries
def install(*packages):
    subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])


try:
    install("pip", "--upgrade")
    install("setuptools", "--upgrade")

    print("Pip upgraded successfully.")
except subprocess.CalledProcessError:
    print("Failed to upgrade pip.")

# Install all required libraries
for lib in required_libraries:
    try:
        install(lib)
        print(f"'{lib}' installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install '{lib}'.")

print("All libraries installed (if available).")
