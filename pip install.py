import subprocess
import sys
import time

# List of required libraries
required_libraries = [
    'pyautogui',
    'pynput',
    'Pillow',  # for PIL
    'mss',
    'discord.py',  # for discord
    'discord',
    'psutil',
    'tkinter',  # tkinter comes with Python, no need to install, but added here for clarity
    'requests',
    'fonttools',  # for fontTools.misc.textTools
    'platform',  # usually comes pre-installed with Python
    'numpy==1.26.2',
    'ultralytics',
    'matplotlib'
]

# Function to install libraries
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install all required libraries
for lib in required_libraries:
    try:
        install(lib)
        print(f"'{lib}' installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install '{lib}'.")

print("All libraries installed (if available).")
print("You can now run the main.py script, everything tried to install")
time.sleep(100)
