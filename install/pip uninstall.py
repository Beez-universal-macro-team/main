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

def uninstall(*packages):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", *packages])

# Uninstall each library in the list
for lib in required_libraries:
    try:
        uninstall(lib)
        print(f"'{lib}' uninstalled successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to uninstall '{lib}'.")

from colorama import init, Fore
init()  # Initialize colorama

print(Fore.GREEN + "All specified libraries uninstalled (if available).")
print(Fore.YELLOW + "You may now run the installation script if needed.")
print(Fore.CYAN + "Press Enter to close..." + Fore.RESET)
input()

