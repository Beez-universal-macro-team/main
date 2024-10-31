from pynput.keyboard import Listener, Key
import gui
import threading
import time
import os

running = False

def check_f2(listener):
    while True:
        if not running:
            time.sleep(0.2)
            continue
        # Check if F2 was pressed through the listener
        if hasattr(listener, 'last_key') and listener.last_key == Key.f2:
            os._exit(0)  # Force exit the entire Python process
        time.sleep(0.2)

def on_release(key):
    global running
    listener.last_key = key
    
    if key == Key.f1:
        if not running:
            running = True
            ui.startMacro(main=True)
    elif key == Key.f2:
        os._exit(0)  # Force exit the entire Python process

# Initialize and start the keyboard listener
listener = Listener(on_release=on_release)
listener.start()

# Start F2 checker thread
f2_thread = threading.Thread(target=check_f2, args=(listener,), daemon=True)
f2_thread.start()

ui = gui.GUI()
ui.initWindow()
ui.saveSettings()

ui.window.mainloop()

