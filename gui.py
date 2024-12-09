import customtkinter as ctk
import tkinter as tk
from matplotlib.mlab import window_none
from functions import offsetDims, screenDims, writeFile, readFile, sendMessage, sendImportantMessage, autoclick
import pyautogui
import altConnection
import os
import socket
import threading
from functions import MainLoopMacro
import ctypes
import time

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
            try:
                if self.clicker_enabled.get():
                    cps = float(self.cps_entry.get())
                    hold = self.hold_enabled.get()
                    autoclick(cps, hold)  # Pass both parameters explicitly
                else:
                    MainLoopMacro()
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to close...")

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
        # Add after other tab definitions
        self.tabControl.add(name='Autoclicker')
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

        self.connect = ctk.CTkButton(self.tabControl.tab('Connecting'), text="Connect new alt",
                                     command=self.connectToAltThread)

        self.settingsTitle = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Settings")
        self.settingsTitle.configure(font=(self.font, 24))

        self.botCheck = tk.BooleanVar(value=False)

        self.botCheckBox = ctk.CTkCheckBox(self.tabControl.tab('Settings'), text="Bot", variable=self.botCheck, onvalue=True, offvalue=False, command=self.checkBotCheckBoxValue)
        self.botCheckBox.pack()
        self.tokenText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Discord Bot Token:")
        self.tokenText.configure(font=(self.font, 14))
        self.botToken = ctk.CTkEntry(self.tabControl.tab('Settings'))

        self.channelIDText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Discord Channel ID:")
        self.channelIDText.configure(font=(self.font, 14))
        self.channelID = ctk.CTkEntry(self.tabControl.tab('Settings'))

        self.webhookText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Discord webhook:")
        self.webhookText.configure(font=(self.font, 14))
        self.webhook = ctk.CTkEntry(self.tabControl.tab('Settings'))
        try:
            self.webhook.insert(0, readFile("guiFiles/webhook.txt"))
        except:
            self.webhook.insert(0, "")


        self.importantWebhookText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Important webhook:")
        self.importantWebhookText.configure(font=(self.font, 14))

        self.importantWebhook = ctk.CTkEntry(self.tabControl.tab('Settings'))

        self.userIdText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Discord user ID:")
        self.userIdText.configure(font=(self.font, 14))

        self.userId = ctk.CTkEntry(self.tabControl.tab('Settings'))

        self.checkBotCheckBoxValue()
        self.botCheckBox.place(relx=0.2, rely=0.11, anchor="n")

        try:
            self.userId.insert(0, readFile("guiFiles/userId.txt"))
        except:
            self.userId.insert(0, "")

        try:
            self.botToken.insert(0, readFile("guiFiles/bot_Token.txt"))
        except:
            self.botToken.insert(0, "")

        try:
            self.channelID.insert(0, readFile("guiFiles/channel_ID.txt"))
        except:
            self.channelID.insert(0, "")

        try:
            self.botCheckBox.select() if eval(readFile("guiFiles/bot_mode.txt")) else self.botCheckBox.deselect()
        except:
            self.botCheckBox.deselect()

        self.moveSpeedText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Base Movespeed:")
        self.moveSpeedText.configure(font=(self.font, 14))

        self.moveSpeed = ctk.CTkEntry(self.tabControl.tab('Settings'))

        try:
            self.moveSpeed.insert(0, readFile("guiFiles/moveSpeed.txt"))
        except:
            self.moveSpeed.insert(0, "33.35")

        try:
            self.importantWebhook.insert(0, readFile("guiFiles/important_webhook.txt"))
        except:
            self.importantWebhook.insert(0, "")

        self.timeoutText = ctk.CTkLabel(self.tabControl.tab('Settings'),
                                        text="Max wait time before reconnecting to alt (minutes):")
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

        self.usingPsBox = ctk.CTkCheckBox(self.tabControl.tab('Private Servers'), text="Use private servers",
                                          variable=self.usingPs, onvalue=1, offvalue=0)

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

        self.vicHoppingButton = ctk.CTkCheckBox(self.tabControl.tab('Vic Hop'), text="Vic Hopping",
                                                variable=self.vicHopping, onvalue=1, offvalue=0)

        self.vicHopping.set(1)

        planters = [
            "PoP",
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
            "Sunflower",
            "Pine Tree",
            "Bamboo",
            "Blue Flower",
            "Stump",
            "Mountain",
            "Cactus",
            "Clover",
        ]

        self.planter1 = ctk.StringVar()
        self.planter2 = ctk.StringVar()
        self.planter3 = ctk.StringVar()

        try:
            self.plantersVals = eval(readFile(os.path.join("guiFiles", "plantersStatus.txt")))

            if self.plantersVals == 0:
                raise ValueError

        except:
            self.plantersVals = {
                "planter1": dict(typ="Heat Treated", field="pepper", status="free", tm="60", tmStarted="0", enabled="0"),
                "planter2": dict(typ="Hydroponic", field="pine", status="free", tm="60", tmStarted="0", enabled="0"),
                "planter3": dict(typ="Petal", field="sunflower", status="free", tm="60", tmStarted="0", enabled="0"),
            }

            writeFile(os.path.join("guiFiles", "plantersStatus.txt"), str(self.plantersVals))

        self.planter1TimeLeft = self.plantersVals["planter1"]["tmStarted"]
        self.planter2TimeLeft = self.plantersVals["planter2"]["tmStarted"]
        self.planter3TimeLeft = self.plantersVals["planter3"]["tmStarted"]

        self.planter1.set(self.plantersVals["planter1"]["typ"])
        self.planter2.set(self.plantersVals["planter2"]["typ"])
        self.planter3.set(self.plantersVals["planter3"]["typ"])

        self.planter1Field = tk.StringVar()
        self.planter2Field = tk.StringVar()
        self.planter3Field = tk.StringVar()

        self.planter1Status = "free"
        self.planter2Status = "free"
        self.planter3Status = "free"

        self.planter1Time = ctk.StringVar(value=self.plantersVals["planter1"]["tm"])
        self.planter2Time = ctk.StringVar(value=self.plantersVals["planter2"]["tm"])
        self.planter3Time = ctk.StringVar(value=self.plantersVals["planter3"]["tm"])

        self.planter1Field.set(self.plantersVals["planter1"]["field"])
        self.planter2Field.set(self.plantersVals["planter2"]["field"])
        self.planter3Field.set(self.plantersVals["planter3"]["field"])

        self.plantersText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Planters")
        self.plantersText.configure(font=(self.font, 24))

        self.planter1Text = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Planter1")
        self.planter2Text = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Planter2")
        self.planter3Text = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Planter3")

        self.planter1Options = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=planters,
                                                 variable=self.planter1)
        self.planter2Options = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=planters,
                                                 variable=self.planter2)
        self.planter3Options = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=planters,
                                                 variable=self.planter3)

        self.planter1FieldText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Field1")
        self.planter2FieldText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Field2")
        self.planter3FieldText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Field3")

        self.planter1Field = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=fields,
                                               variable=self.planter1Field)
        self.planter2Field = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=fields,
                                               variable=self.planter2Field)
        self.planter3Field = ctk.CTkOptionMenu(self.tabControl.tab('Planters'), values=fields,
                                               variable=self.planter3Field)

        self.planter1TimeText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Time1")
        self.planter2TimeText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Time2")
        self.planter3TimeText = ctk.CTkLabel(self.tabControl.tab('Planters'), text="Time3")

        self.planter1TimeEntry = ctk.CTkEntry(self.tabControl.tab('Planters'), textvariable=self.planter1Time)
        self.planter2TimeEntry = ctk.CTkEntry(self.tabControl.tab('Planters'), textvariable=self.planter2Time)
        self.planter3TimeEntry = ctk.CTkEntry(self.tabControl.tab('Planters'), textvariable=self.planter3Time)

        self.planter1Enabled = ctk.StringVar(value="0")
        self.planter2Enabled = ctk.StringVar(value="0")
        self.planter3Enabled = ctk.StringVar(value="0")

        self.planter1Enabled.set(self.plantersVals["planter1"]["enabled"])
        self.planter2Enabled.set(self.plantersVals["planter2"]["enabled"])
        self.planter3Enabled.set(self.plantersVals["planter3"]["enabled"])

        self.planter1EnabledCheckbox = ctk.CTkCheckBox(self.tabControl.tab('Planters'), text="Planter1", variable=self.planter1Enabled, onvalue="1", offvalue="0")
        self.planter2EnabledCheckbox = ctk.CTkCheckBox(self.tabControl.tab('Planters'), text="Planter2",
                                                       variable=self.planter2Enabled, onvalue="1", offvalue="0")
        self.planter3EnabledCheckbox = ctk.CTkCheckBox(self.tabControl.tab('Planters'), text="Planter3",
                                                       variable=self.planter3Enabled, onvalue="1", offvalue="0")

        self.cps_label = ctk.CTkLabel(self.tabControl.tab('Autoclicker'), text="CPS (Clicks per second):")
        self.cps_label.pack(pady=10)

        self.cps_entry = ctk.CTkEntry(self.tabControl.tab('Autoclicker'))
        self.cps_entry.pack(pady=5)
        self.cps_entry.insert(0, "10")  # Default CPS value

        self.clicker_enabled = tk.BooleanVar()
        self.clicker_checkbox = ctk.CTkCheckBox(self.tabControl.tab('Autoclicker'),
                                            text="Enable Autoclicker", 
                                            variable=self.clicker_enabled)
        self.clicker_checkbox.pack(pady=10)

        self.hold_enabled = tk.BooleanVar()
        self.hold_checkbox = ctk.CTkCheckBox(self.tabControl.tab('Autoclicker'),
                                        text="Hold Instead of Click", 
                                        variable=self.hold_enabled)
        self.hold_checkbox.pack(pady=10)


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

        self.planter1TimeText.pack()
        self.planter2TimeText.pack()
        self.planter3TimeText.pack()

        self.planter1TimeText.place(relx=0.2, rely=0.595, anchor="n")
        self.planter2TimeText.place(relx=0.5, rely=0.595, anchor="n")
        self.planter3TimeText.place(relx=0.8, rely=0.595, anchor="n")

        self.planter1TimeEntry.pack()
        self.planter2TimeEntry.pack()
        self.planter3TimeEntry.pack()

        self.planter1TimeEntry.place(relx=0.2, rely=0.68, anchor="n")
        self.planter2TimeEntry.place(relx=0.5, rely=0.68, anchor="n")
        self.planter3TimeEntry.place(relx=0.8, rely=0.68, anchor="n")

        self.planter1EnabledCheckbox.pack()
        self.planter2EnabledCheckbox.pack()
        self.planter3EnabledCheckbox.pack()

        self.planter1EnabledCheckbox.place(relx=0.2, rely=0.1, anchor="n")
        self.planter2EnabledCheckbox.place(relx=0.5, rely=0.1, anchor="n")
        self.planter3EnabledCheckbox.place(relx=0.8, rely=0.1, anchor="n")

        self.saveSettings()

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
        plantersStatus = eval(readFile(os.path.join("guiFiles", "plantersStatus.txt")))

        self.planter1Status = plantersStatus["planter1"]["status"]
        self.planter2Status = plantersStatus["planter2"]["status"]
        self.planter3Status = plantersStatus["planter3"]["status"]

        self.planter1Time.set(plantersStatus["planter1"]["tmStarted"])
        self.planter2Time.set(plantersStatus["planter2"]["tmStarted"])
        self.planter3Time.set(plantersStatus["planter3"]["tmStarted"])
        
        self.plantersVals = {
            "planter1": dict(typ=self.planter1.get(), field=self.planter1Field.get(), status=self.planter1Status, tm=self.planter1Time.get(), tmStarted=self.planter1TimeLeft, enabled=self.planter1Enabled.get()),
            "planter2": dict(typ=self.planter2.get(), field=self.planter2Field.get(), status=self.planter2Status, tm=self.planter2Time.get(), tmStarted=self.planter2TimeLeft, enabled=self.planter2Enabled.get()),
            "planter3": dict(typ=self.planter3.get(), field=self.planter3Field.get(), status=self.planter3Status, tm=self.planter3Time.get(), tmStarted=self.planter3TimeLeft, enabled=self.planter3Enabled.get())
        }

        writeFile(os.path.join("guiFiles", "plantersStatus.txt"), str(self.plantersVals))

    def saveWindowSize(self):
        x, y = self.window.winfo_width(), self.window.winfo_height()

        writeFile("guiFiles/windowSize.txt", f"{self.window.winfo_width()}x{self.window.winfo_height()}")

    def getPrivateServer(self, n):
        privateServers = eval(readFile("guiFiles/privateServers.txt"))

        return privateServers[n]
        
    def botTokenChange(self):
        botToken = self.botToken.get()
        writeFile("guiFiles/bot_Token.txt", botToken)

    def channelIDChange(self):
        channelID = self.channelID.get()
        writeFile("guiFiles/channel_ID.txt", channelID)

    def botModeChange(self):
        writeFile("guiFiles/bot_mode.txt", str(self.botCheckBox.get()))

    
    def startMacro(self, main=False):
        self.saveSettings()
        if not main:
            self.macro_thread = threading.Thread(target=self.startMacro, args=(True,))
            self.macro_thread.start()
        else:
            try:
                if self.clicker_enabled.get():
                    cps = float(self.cps_entry.get())
                    hold = self.hold_enabled.get()
                    autoclick(cps, hold)  # Pass both parameters explicitly
                else:
                    MainLoopMacro()
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to close...")



    def stopMacro(self):
        quit()

    def connectToAltThread(self):
        port = int(pyautogui.prompt(text='Port connecting to new alt?', title='Pls answer...', default=''))

        self.t = threading.Thread(target=self.connectToAlt, args=(port,))

        self.t.daemon = True

        self.t.start()

    def connectToAlt(self, port):
        self.AltConnection = altConnection.AltConnection(port)

        try:
            self.ip, self.port = self.AltConnection.connectToAlt()

            # pyautogui.alert(f"Recieved connection from {self.ip} port {self.port}")

            self.AltConnection.recieveNightServers(timeout=int(self.timeout.get()) * 60)

        except:
            sendMessage("Alt connection failed...")

            pyautogui.alert("Alt connection failed...")

    def checkBotCheckBoxValue(self):
        if self.botCheckBox.get():
            self.webhookText.place_forget()
            self.webhook.place_forget()
            self.tokenText.place(relx=0.15, rely=0.19, anchor="n")
            self.botToken.place(relx=0.15, rely=0.27, anchor="n")
            self.channelIDText.place(relx=0.15, rely=0.40, anchor="n")
            self.channelID.place(relx=0.15, rely=0.48, anchor="n")
        else:
            self.tokenText.place_forget()
            self.botToken.place_forget()
            self.channelIDText.place_forget()
            self.channelID.place_forget()
            self.webhookText.place(relx=0.15, rely=0.19, anchor="n")
            self.webhook.place(relx=0.15, rely=0.27, anchor="n")



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
        self.botTokenChange()
        self.channelIDChange()
        self.botModeChange()
        self.plantersChange()

        self.window.after(1000, self.saveSettings)
