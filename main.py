from pynput.keyboard import Listener, Key
import gui
import threading
import time
import os

running = False

def check_f2():
    listener = Listener(on_press=lambda key: key == Key.f2 and os._exit(0))
    listener.start()
    listener.join()

def on_release(key):
    global running
    if key == Key.f1:
        if not running:
            running = True
            ui.startMacro(main=True)
    elif key == Key.f2:
        ui.saveSettings()
        os._exit(0)

# Start F2 checker thread with dedicated listener
f2_thread = threading.Thread(target=check_f2, daemon=True)
f2_thread.start()

# Main listener for other keys
listener = Listener(on_release=on_release)
listener.start()

ui = gui.GUI()
ui.initWindow()
ui.saveSettings()

ui.window.mainloop()


ui.window.mainloop()



ui.window.mainloop()

