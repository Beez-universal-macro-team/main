from pynput.keyboard import Listener, Key
import gui

running = False

def on_release(key):
    global running
    
    if key == Key.f1:
        if not running:
            running = True

            ui.startMacro(main=True)

    elif key == Key.f2:
        listener.stop()

        ui.window.quit()

listener = Listener(on_release=on_release)
listener.start()

ui = gui.GUI()

ui.initWindow()
ui.saveSettings()

ui.window.mainloop()
