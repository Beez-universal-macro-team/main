import customtkinter as ctk
import tkinter as tk
from matplotlib.mlab import window_none
from functions import offsetDims, screenDims, writeFile, readFile, sendMessage, sendImportantMessage
import pyautogui
import altConnection
import os
import socket
import threading
from functions import MainLoopMacro
import ctypes

main_dir = os.path.dirname(os.path.abspath(__file__))

class GUI:
    def __init__(self, font="Courier"):
        self.font = font
        self.connected = False
        self.macro_thread = None

    def f3_pressed(self):
        if self.macro_thread and self.macro_thread.is_alive():
            ctypes.pythonapi.PyThreadState_SetAsyncExc(self.macro_thread.ident, ctypes.py_object(SystemExit))
            
        try:
            keyboard.release("w")
            keyboard.release("d")
            keyboard.release("a")
            keyboard.release("s")
        except:
            pass
        os._exit(0)

    def f2_pressed(self):
        if self.macro_thread and self.macro_thread.is_alive():
            ctypes.pythonapi.PyThreadState_SetAsyncExc(self.macro_thread.ident, ctypes.py_object(SystemExit))
            
        try:
            keyboard.release("w")
            keyboard.release("d")
            keyboard.release("a")
            keyboard.release("s")
        except:
            pass

    def startMacro(self, main=False):
        self.saveSettings()
        if not main:
            self.macro_thread = threading.Thread(target=self.startMacro, args=(True,))
            self.macro_thread.start()
        else:
            self.macro_thread = threading.current_thread()
            MainLoopMacro()

    def initWindow(self):
        sendMessage("Started main!")
        sendImportantMessage("Started main!")
        
        self.window = ctk.CTk()

        self.window.title("Beez Universal Macro - Main")

        # Set the GUI logo
        logo_path = os.path.join(main_dir, "basicbeeface.ico")

        self.window.iconbitmap(logo_path)        
        self.window.geometry(f"{max(offsetDims(700, 'x'), 700)}x{max(offsetDims(350, 'y'), 350)}")
        self.window.minsize(700, 350)

        ###### CREATING TABS ######

        self.tabControl = ctk.CTkTabview(self.window)

        self.tabControl.add(name='Join Settings')
        self.tabControl.add(name='Vic Hop')
        self.tabControl.add(name='Connecting')
        self.tabControl.add(name='Settings')
        self.tabControl.add(name='Private Servers')
        self.tabControl.add(name='Planters')
        self.tabControl.add(name='Credits')

        ###### CREATING TEXT ######

        for i in range(1, 6):
            globals()[f"self.{i}"] = 0

        self.maxLoadTime = tk.StringVar()

        self.joinTitle = ctk.CTkLabel(self.tabControl.tab('Join Settings'), text="Join Settings")
        self.joinTitle.configure(font=(self.font, 24))

        self.maxLoadText = ctk.CTkLabel(self.tabControl.tab('Join Settings'), text="Maximum load time:")
        self.maxLoadText.configure(font=(self.font, 14))

        self.maxLoad = ctk.CTkEntry(self.tabControl.tab('Join Settings'), width=40)

        try:
            self.maxLoad.insert(0, readFile("guiFiles/maxLoadTime.txt"))
        except:
            self.maxLoad.insert(0, "25")

        self.start = ctk.CTkButton(self.window, text="Start (f1)", command=self.startMacro)
        self.stop = ctk.CTkButton(self.window, text="Exit (f3)", command=self.f3_pressed)
        self.exit = ctk.CTkButton(self.window, text="Stop (f2)", command=self.f2_pressed)

        self.connect = ctk.CTkButton(self.tabControl.tab('Connecting'), text="Connect new alt", command=self.connectToAltThread)

        self.settingsTitle = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Settings")
        self.settingsTitle.configure(font=(self.font, 24))

        self.webhookText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Discord webhook:")
        self.webhookText.configure(font=(self.font, 14))

        self.webhook = ctk.CTkEntry(self.tabControl.tab('Settings'))

        self.importantWebhookText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Important webhook:")
        self.importantWebhookText.configure(font=(self.font, 14))

        self.importantWebhook = ctk.CTkEntry(self.tabControl.tab('Settings'))

        self.userIdText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Discord user ID:")
        self.userIdText.configure(font=(self.font, 14))

        self.userId = ctk.CTkEntry(self.tabControl.tab('Settings'))

        try:
            self.userId.insert(0, readFile("guiFiles/userId.txt"))
        except:
            self.userId.insert(0, "")

        self.moveSpeedText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Base Movespeed:")
        self.moveSpeedText.configure(font=(self.font, 14))

        self.moveSpeed = ctk.CTkEntry(self.tabControl.tab('Settings'))

        try:
            self.moveSpeed.insert(0, readFile("guiFiles/moveSpeed.txt"))
        except:
            self.moveSpeed.insert(0, "")

        try:
            self.importantWebhook.insert(0, readFile("guiFiles/important_webhook.txt"))
        except:
            self.importantWebhook.insert(0, "")


        self.timeoutText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Max wait time before reconnecting to alt (minutes):")
        self.timeoutText.configure(font=(self.font, 14))

        self.timeout = ctk.CTkEntry(self.tabControl.tab('Settings'))

        try:
            self.timeout.insert(0, readFile("guiFiles/timeout.txt"))
        except:
            self.timeout.insert(0, "20")

        try:
            self.webhook.insert(0, readFile("guiFiles/webhook.txt"))
        except:
            self.webhook.insert(0, "")

        self.confidenceText = ctk.CTkLabel(self.tabControl.tab('Settings'),
                                        text="Claim hive detection confidence:")
        self.confidenceText.configure(font=(self.font, 14))

        self.confidence = ctk.CTkEntry(self.tabControl.tab('Settings'))

        try:
            self.confidence.insert(0, readFile("guiFiles/confidence.txt"))
        except:
            self.confidence.insert(0, "0.7")

        self.connectingText = ctk.CTkLabel(self.tabControl.tab('Connecting'), text="Connecting")
        self.connectingText.configure(font=(self.font, 24))

        self.hostNameText = ctk.CTkLabel(self.tabControl.tab('Connecting'), text="Host name:")
        self.hostNameText.configure(font=(self.font, 17))

        self.hostName = ctk.CTkLabel(self.tabControl.tab('Connecting'), text=socket.gethostname())
        self.hostName.configure(font=(self.font, 14))

        self.privateServersText = ctk.CTkLabel(self.tabControl.tab('Private Servers'), text="Private servers")
        self.privateServersText.configure(font=(self.font, 24))

        for i in range(1, 6):
            globals()[f"self.{i}"] = ctk.CTkEntry(self.tabControl.tab('Private Servers'))

            try:
                globals()[f"self.{i}"].insert(0, self.getPrivateServer(i - 1))

            except:
                pass

        self.usingPs = tk.IntVar(self.tabControl.tab('Private Servers'))

        self.usingPsBox = ctk.CTkCheckBox(self.tabControl.tab('Private Servers'), text="Use private servers", variable=self.usingPs, onvalue=1, offvalue=0)

        try:
            self.usingPs.set(1 if eval(readFile("guiFiles/joinPrivateServers.txt")) else 0)

        except:
            pass

        owner = "Beez131"

        contributors = [
            "Sharkboy1663",
            "Pirosow"
        ]

        specialThanks = [
            "Slymi",
            "_epic",
            "Fire_king66",
            "Lvl18BubbleBee"
        ]

        self.ownerText = ctk.CTkLabel(self.tabControl.tab('Credits'), text="Owner/Head Developer:")
        self.ownerText.configure(font=(self.font, 15))

        self.owner = ctk.CTkLabel(self.tabControl.tab('Credits'), text=owner)

        self.contributors = ctk.CTkLabel(self.tabControl.tab('Credits'), text="Developers:")
        self.contributors.configure(font=(self.font, 15))

        for contributor in contributors:
            globals()[f"self.{contributor}"] = ctk.CTkLabel(self.tabControl.tab('Credits'), text=contributor)

        self.specialThanks = ctk.CTkLabel(self.tabControl.tab('Credits'), text="Special Thanks To:")
        self.specialThanks.configure(font=(self.font, 15))

        for specialThank in specialThanks:
            globals()[f"self.{specialThank}"] = ctk.CTkLabel(self.tabControl.tab('Credits'), text=specialThank)

        self.vicHopText = ctk.CTkLabel(self.tabControl.tab('Vic Hop'), text="Vic Hop")
        self.vicHopText.configure(font=(self.font, 24))

        self.vicHopping = tk.IntVar()

        self.vicHoppingButton = ctk.CTkCheckBox(self.tabControl.tab('Vic Hop'), text="Vic Hopping", variable=self.vicHopping, onvalue=1, offvalue=0)

        self.vicHopping.set(1)


        planters = [
            "Heat Treated",
            "Hydroponic",
            "Petal",
            "Red Clay",
            "Blue Clay",
            "Pesticide",
            "Tacky",
            "Candy",
            "Plastic",
        ]

        fields = [
            "Pepper",
            "Rose",
            "Strawberry",
            "Mushroom",
            "Coconut",
            "Spider",
            "Pumpkin",
            "Pineapple",
            "Dandelion",
            "Sunflower"
            "Mountain",
            "Cactus",
            "Clover",
        ]

        self.planter1 = ctk.StringVar()
        self.planter2 = ctk.StringVar()
        self.planter3 = ctk.StringVar()

        try:
            self.plantersVals = eval(readFile("guiFiles/planters.txt"))

            if self.plantersVals == 0:
                raise ValueError

        except:
            self.plantersVals = ["Heat Treated", "Hydroponic", "Petal"]

        try:
            self.plantersFields = eval(readFile("guiFiles/planterFields.txt"))

            if self.plantersFields == 0:
                raise ValueError

        except:
            self.plantersFields = ["Pepper", "BlueFlower", "Sunflower"]

        print(self.plantersVals)

        self.planter1.set(self.plantersVals[0])
        self.planter2.set(self.plantersVals[1])
        self.planter3.set(self.plantersVals[2])

        self.planter1Field = tk.StringVar()
        self.planter2Field = tk.StringVar()
        self.planter3Field = tk.StringVar()

        self.planter1Field.set(self.plantersFields[0])
        self.planter2Field.set(self.plantersFields[1])
        self.planter3Field.set(self.plantersFields[2])

        self.plantersText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Planters")
        self.plantersText.configure(font=(self.font, 24))

        self.planter1Text = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Planter1")
        self.planter2Text = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Planter2")
        self.planter3Text = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Planter3")

        self.planter1Options = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=planters, variable=self.planter1)
        self.planter2Options = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=planters, variable=self.planter2)
        self.planter3Options = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=planters, variable=self.planter3)

        self.planter1FieldText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Field1")
        self.planter2FieldText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Field2")
        self.planter3FieldText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Field3")

        self.planter1Field = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=fields, variable=self.planter1Field)
        self.planter2Field = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=fields, variable=self.planter2Field)
        self.planter3Field = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=fields, variable=self.planter3Field)
        
        ###### DISPLAYING TEXT ######

        self.tabControl.pack(expand=2, fill="both")

        self.joinTitle.pack()
        self.maxLoadText.pack()
        self.maxLoad.pack()
        self.maxLoadText.place(relx=0.5, rely=0.3, anchor="n")
        self.maxLoad.place(relx=0.5, rely=0.38, anchor="n")

        self.start.pack()
        self.start.place(relx=0.25, rely=0.8, anchor="n")

        self.exit.pack()
        self.exit.place(relx=0.5, rely=0.8, anchor="n")

        self.stop.pack()
        self.stop.place(relx=0.75, rely=0.8, anchor="n")
        self.settingsTitle.pack()

        self.webhookText.pack()
        self.webhook.pack()

        self.importantWebhookText.pack()
        self.importantWebhook.pack() 
        self.importantWebhookText.place(relx=0.8, rely=0.11, anchor="n")
        self.importantWebhook.place(relx=0.8, rely=0.19, anchor="n")


        self.userIdText.pack()
        self.userId.pack()

        self.confidenceText.pack()
        self.confidence.pack()

        self.moveSpeedText.pack()
        self.moveSpeed.pack()

        self.timeoutText.pack()
        self.timeout.pack()

        self.connectingText.pack()

        self.hostNameText.pack()
        self.hostName.pack()

        self.hostNameText.place(relx=0.5, rely=0.25, anchor="n")
        self.hostName.place(relx=0.5, rely=0.32, anchor="n")

        self.connect.pack()
        self.connect.place(relx=0.5, rely=0.45, anchor="n")

        self.privateServersText.pack()

        for i in range(5):
            globals()[f"self.{i + 1}"].pack()

        self.usingPsBox.pack()

        self.ownerText.pack()
        self.owner.pack()

        self.contributors.pack()

        for contributor in contributors:
            globals()[f"self.{contributor}"].pack()

        self.specialThanks.pack()

        for specialThank in specialThanks:
            globals()[f"self.{specialThank}"].pack()

        self.vicHopText.pack()

        self.vicHoppingButton.pack()

        self.confidenceText.place(relx=0.8, rely=0.45, anchor="n")
        self.confidence.place(relx=0.8, rely=0.53, anchor="n")

        self.beesmasText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Beesmas:")
        self.beesmasText.configure(font=(self.font, 14))

        self.beesmas = tk.IntVar(self.tabControl.tab('Settings'))
        self.beesmasBox = ctk.CTkCheckBox(self.tabControl.tab('Settings'), 
                                        text="Enable Beesmas", 
                                        variable=self.beesmas)

        try:
            self.beesmas.set(1 if eval(readFile("guiFiles/beesmasToggle.txt")) else 0)
        except:
            pass

        # Place them
        self.beesmasText.place(relx=0.8, rely=0.3, anchor="n")
        self.beesmasBox.place(relx=0.8, rely=0.38, anchor="n")


        self.plantersText.pack()

        self.planter1Text.pack()
        self.planter2Text.pack()
        self.planter3Text.pack()

        self.planter1Text.place(relx=0.2, rely=0.215, anchor="n")
        self.planter2Text.place(relx=0.5, rely=0.215, anchor="n")
        self.planter3Text.place(relx=0.8, rely=0.215, anchor="n")

        self.planter1Options.pack()
        self.planter2Options.pack()
        self.planter3Options.pack()

        self.planter1Options.place(relx=0.2, rely=0.3, anchor="n")
        self.planter2Options.place(relx=0.5, rely=0.3, anchor="n")
        self.planter3Options.place(relx=0.8, rely=0.3, anchor="n")

        self.planter1FieldText.pack()
        self.planter2FieldText.pack()
        self.planter3FieldText.pack()

        self.planter1FieldText.place(relx=0.2, rely=0.415, anchor="n")
        self.planter2FieldText.place(relx=0.5, rely=0.415, anchor="n")
        self.planter3FieldText.place(relx=0.8, rely=0.415, anchor="n")

        self.planter1Field.pack()
        self.planter2Field.pack()
        self.planter3Field.pack()

        self.planter1Field.place(relx=0.2, rely=0.5, anchor="n")
        self.planter2Field.place(relx=0.5, rely=0.5, anchor="n")
        self.planter3Field.place(relx=0.8, rely=0.5, anchor="n")


    # Add to saveSettings method
    def beesmasChange(self):
        writeFile("guiFiles/beesmasToggle.txt", True if self.beesmas.get() else False)



    def maxLoadTimeChange(self):
        tm = self.maxLoad.get()

        if str(tm).isnumeric():
            writeFile("guiFiles/maxLoadTime.txt", tm)

        else:
            pyautogui.alert("Make sure to set max load time to a number!")

    def webhookChange(self):
        webhook = self.webhook.get()

        writeFile("guiFiles/webhook.txt", webhook)


    def importantWebhookChange(self):
        important_webhook = self.importantWebhook.get()
        writeFile("guiFiles/important_webhook.txt", important_webhook)

    def privateServersChange(self):
        privateServers = []

        for i in range(5):
            privateServer = globals()[f"self.{i + 1}"].get()

            privateServers.append(privateServer)

        writeFile("guiFiles/privateServers.txt", str(privateServers))
        writeFile("guiFiles/joinPrivateServers.txt", True if self.usingPs.get() else False)

    def userIdChange(self):
        userId = self.userId.get()

        writeFile("guiFiles/userId.txt", userId)

    def confidenceChange(self):
        confidence = self.confidence.get()

        writeFile("guiFiles/confidence.txt", confidence)

    def moveSpeedChange(self):
        moveSpeed = self.moveSpeed.get()

        writeFile("guiFiles/moveSpeed.txt", moveSpeed)

    def timeoutChange(self):
        timeout = self.timeout.get()

        writeFile("guiFiles/timeout.txt", timeout)

    def plantersChange(self):
        plantersVals = [self.planter1.get(), self.planter2.get(), self.planter3.get()]
        plantersFields = [self.planter1Field.get(), self.planter2Field.get(), self.planter3Field.get()]

        writeFile("guiFiles/planters.txt", str(plantersVals))
        writeFile("guiFiles/planterFields.txt", str(plantersFields))

    def saveWindowSize(self):
        x, y = self.window.winfo_width(), self.window.winfo_height()

        writeFile("guiFiles/windowSize.txt", f"{self.window.winfo_width()}x{self.window.winfo_height()}")

    def getPrivateServer(self, n):
        privateServers = eval(readFile("guiFiles/privateServers.txt"))

        return privateServers[n]


    def startMacro(self, main=False):
        self.saveSettings()

        try:
            # Your main code here
            MainLoopMacro()
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to close...")  # This keeps terminal open

    def stopMacro(self):
        quit()

    def connectToAltThread(self):
        port = int(pyautogui.prompt(text='Port connecting to new alt?', title='Pls answer...' , default=''))

        self.t = threading.Thread(target=self.connectToAlt, args=(port,))

        self.t.daemon = True

        self.t.start()

    def connectToAlt(self, port):
        self.AltConnection = altConnection.AltConnection(port)

        try:
            self.ip, self.port = self.AltConnection.connectToAlt()

            #pyautogui.alert(f"Recieved connection from {self.ip} port {self.port}")

            self.AltConnection.recieveNightServers(timeout=int(self.timeout.get()) * 60)

        except:
            sendMessage("Alt connection failed...")

            pyautogui.alert("Alt connection failed...")

    def saveSettings(self):
        self.maxLoadTimeChange()
        self.webhookChange()
        self.privateServersChange()
        self.userIdChange()
        self.confidenceChange()
        self.moveSpeedChange()
        self.timeoutChange()
        self.beesmasChange()
        self.saveWindowSize()
        self.importantWebhookChange()
        self.plantersChange()

        self.window.after(1000, self.saveSettings)
