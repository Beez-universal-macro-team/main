from pynput.keyboard import Listener, Key, Controller as keyboardController
import gui
import threading
import time
import os
import ctypes

keyboard = keyboardController()
running = False
macro_thread = None

def monitor_f2():
    def on_press(key):
        if key == Key.f2:
            global macro_thread, running
            if macro_thread and macro_thread.is_alive():
                ctypes.pythonapi.PyThreadState_SetAsyncExc(macro_thread.ident, ctypes.py_object(SystemExit))
                running = False
            
            try:
                keyboard.release("w")
                keyboard.release("d")
                keyboard.release("a")
                keyboard.release("s")
            except:
                pass

            ui.saveSettings()
    
    with Listener(on_press=on_press) as f2_listener:
        f2_listener.join()

def monitor_f3():
    def on_press(key):
        if key == Key.f3:
            global macro_thread, running
            if macro_thread and macro_thread.is_alive():
                ctypes.pythonapi.PyThreadState_SetAsyncExc(macro_thread.ident, ctypes.py_object(SystemExit))
                running = False
            
            try:
                keyboard.release("w")
                keyboard.release("d")
                keyboard.release("a")
                keyboard.release("s")
            except:
                pass
            os._exit(0)
    
    with Listener(on_press=on_press) as f3_listener:
        f3_listener.join()

def on_release(key):
    global running, macro_thread
    if key == Key.f1:
        if not running:
            running = True
            macro_thread = threading.Thread(target=ui.startMacro, args=(True,))
            macro_thread.start()

# Start dedicated monitor threads
f2_thread = threading.Thread(target=monitor_f2, daemon=True)
f2_thread.start()

f3_thread = threading.Thread(target=monitor_f3, daemon=True)
f3_thread.start()

# Main listener for F1
listener = Listener(on_release=on_release)
listener.daemon = True
listener.start()

ui = gui.GUI()
ui.initWindow()
ui.saveSettings()

ui.window.mainloop()

