from pynput.keyboard import Listener, Key
import gui
import threading
import time
import keyboard
import sys
import os

running = False

def check_f2():
    while True:
        if keyboard.is_pressed('f2'):
            os._exit(0)  # Force exit the entire Python process
        time.sleep(0.2)

def on_release(key):
    global running
    
    if key == Key.f1:
        if not running:
            running = True
            ui.startMacro(main=True)
    elif key == Key.f2:
        os._exit(0)  # Force exit the entire Python process

# Start F2 checker thread
f2_thread = threading.Thread(target=check_f2, daemon=True)
f2_thread.start()

listener = Listener(on_release=on_release)
listener.start()

ui = gui.GUI()
ui.initWindow()
ui.saveSettings()

ui.window.mainloop()
