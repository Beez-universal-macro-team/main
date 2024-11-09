import subprocess
import sys

# List of libraries to uninstall
libraries_to_uninstall = [
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
    'opencv-python',
    'numpy',
    'colorama',
    'ImageHash',
    'pyautogui',  # Added pyautogui
]

def uninstall(*packages):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", *packages])

# First uninstall all libraries in the list
for lib in libraries_to_uninstall:
    try:
        uninstall(lib)
        print(f"'{lib}' uninstalled successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to uninstall '{lib}' or it was not found.")

print("All specified libraries uninstalled (if installed).")
print("You can now run the install script again to re-install them.")
print("Press Enter to close...")
input()
