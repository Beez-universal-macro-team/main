import tkinter as tk
from functions import offsetDims, screenDims, writeFile, readFile, sendMessage
import pyautogui
import altConnection
import os
import socket
import threading

main_dir = os.path.dirname(os.path.abspath(__file__))

class GUI:
    def __init__(self, font="Courier"):
        self.font = font

        self.connected = False

    def initWindow(self):
        sendMessage("Started main!")
        
        self.window = tk.Tk()

        self.window.title("Beez Universal Macro - Main")

        # Set the GUI logo
        logo_path = os.path.join(main_dir, "basicbeeface.ico")
        self.window.iconbitmap(logo_path)
        
        self.window.geometry(f"{offsetDims(700, 'x')}x{offsetDims(350, 'y')}")

        self.window.resizable(False, False) #Locks GUI size

        ###### CREATING TABS ######

        self.tabControl = tk.ttk.Notebook(self.window)

        self.joinSettingsTab = tk.ttk.Frame(self.tabControl)
        self.connectTab = tk.ttk.Frame(self.tabControl)
        self.settingsTab = tk.ttk.Frame(self.tabControl)
        self.privateServersTab = tk.ttk.Frame(self.tabControl)
        self.creditsTab = tk.ttk.Frame(self.tabControl)
        self.vicTab = tk.ttk.Frame(self.tabControl)

        self.tabControl.add(self.joinSettingsTab, text='Join Settings')
        self.tabControl.add(self.vicTab, text='Vic Hop')
        self.tabControl.add(self.connectTab, text='Connecting')
        self.tabControl.add(self.settingsTab, text='Settings')
        self.tabControl.add(self.privateServersTab, text='Private Servers')
        self.tabControl.add(self.creditsTab, text='Credits')

        ###### CREATING TEXT ######

        for i in range(1, 6):
            globals()[f"self.{i}"] = 0

        self.maxLoadTime = tk.StringVar()

        self.joinTitle = tk.Label(self.joinSettingsTab, text="Join Settings")
        self.joinTitle.config(font=(self.font, 17))

        self.maxLoadText = tk.Label(self.joinSettingsTab, text="Maximum load time:")
        self.maxLoadText.config(font=(self.font, 14))

        self.maxLoad = tk.Entry(self.joinSettingsTab, width=3)

        try:
            self.maxLoad.insert(0, readFile("guiFiles/maxLoadTime.txt"))
        except:
            self.maxLoad.insert(0, "10")

        self.start = tk.Button(self.window, text="Start (f1)", command=self.startMacro)
        self.stop = tk.Button(self.window, text="Stop (f2)", command=self.stopMacro)

        self.connect = tk.Button(self.connectTab, text="Connect new alt", command=self.connectToAltThread)

        self.settingsTitle = tk.Label(self.settingsTab, text="Settings")
        self.settingsTitle.config(font=(self.font, 17))

        self.webhookText = tk.Label(self.settingsTab, text="Discord webhook:")
        self.webhookText.config(font=(self.font, 14))

        self.webhook = tk.Entry(self.settingsTab)

        try:
            self.webhook.insert(0, readFile("guiFiles/webhook.txt"))
        except:
            self.webhook.insert(0, "")

        self.connectingText = tk.Label(self.connectTab, text="Connecting")
        self.connectingText.config(font=(self.font, 14))

        self.hostNameText = tk.Label(self.connectTab, text="Host name:")
        self.hostNameText.config(font=(self.font, 14))

        self.hostName = tk.Label(self.connectTab, text=socket.gethostname())
        self.hostName.config(font=(self.font, 14))

        self.privateServersText = tk.Label(self.privateServersTab, text="Private servers")
        self.privateServersText.config(font=(self.font, 14))

        for i in range(1, 6):
            globals()[f"self.{i}"] = tk.Entry(self.privateServersTab)

            try:
                globals()[f"self.{i}"].insert(0, self.getPrivateServer(i - 1))

            except:
                pass

        self.usingPs = tk.IntVar(self.privateServersTab)

        self.usingPsBox = tk.Checkbutton(self.privateServersTab, text="Use private servers", variable=self.usingPs, onvalue=1, offvalue=0)

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
        ]

        self.ownerText = tk.Label(self.creditsTab, text="Owner/Head Developer:")
        self.ownerText.config(font=(self.font, 15))

        self.owner = tk.Label(self.creditsTab, text=owner)

        self.contributors = tk.Label(self.creditsTab, text="Developers:")
        self.contributors.config(font=(self.font, 15))

        for contributor in contributors:
            globals()[f"self.{contributor}"] = tk.Label(self.creditsTab, text=contributor)

        self.specialThanks = tk.Label(self.creditsTab, text="Special Thanks To:")
        self.specialThanks.config(font=(self.font, 15))

        for specialThank in specialThanks:
            globals()[f"self.{specialThank}"] = tk.Label(self.creditsTab, text=specialThank)

        self.vicHopText = tk.Label(self.vicTab, text="Vic Hop")
        self.vicHopText.config(font=(self.font, 20))

        self.vicHopping = tk.IntVar(self.vicTab)

        self.vicHoppingButton = tk.Checkbutton(self.vicTab, text="Vic Hopping", variable=self.vicHopping, onvalue=1, offvalue=0)

        self.vicHopping.set(1)

        self.checkByWalking = tk.Label(self.vicTab, text="Check vic bee by walking in field:")
        self.checkByWalking.config(font=(self.font, 14))

        self.walkInPepper = tk.IntVar(self.vicTab)
        self.walkInRose = tk.IntVar(self.vicTab)
        self.walkInMountain = tk.IntVar(self.vicTab)
        self.walkInCactus = tk.IntVar(self.vicTab)
        self.walkInSpider = tk.IntVar(self.vicTab)

        self.pepperWalk = tk.Checkbutton(self.vicTab, text="Walk to pepper field", variable=self.walkInPepper, onvalue=1, offvalue=0)
        self.roseWalk = tk.Checkbutton(self.vicTab, text="Walk to rose field", variable=self.walkInRose, onvalue=1, offvalue=0)
        self.mountainWalk = tk.Checkbutton(self.vicTab, text="Walk to mountain field", variable=self.walkInMountain, onvalue=1, offvalue=0)
        self.cactusWalk = tk.Checkbutton(self.vicTab, text="Walk to cactus field", variable=self.walkInCactus, onvalue=1, offvalue=0)
        self.spiderWalk = tk.Checkbutton(self.vicTab, text="Walk to spider field", variable=self.walkInSpider, onvalue=1, offvalue=0)

        ###### DISPLAYING TEXT ######

        self.tabControl.pack(expand=2, fill="both")

        self.joinTitle.pack()

        self.maxLoadText.pack()
        self.maxLoad.pack()

        self.maxLoadText.place(relx=0.5, rely=0.35, anchor="n")
        self.maxLoad.place(relx=0.5, rely=0.5, anchor="n")

        self.start.pack()
        self.start.place(relx=0.35, rely=0.8, anchor="n")

        self.stop.pack()
        self.stop.place(relx=0.65, rely=0.8, anchor="n")

        self.settingsTitle.pack()

        self.webhookText.pack()
        self.webhook.pack()

        self.connectingText.pack()

        tk.Label(self.connectTab, text=" ").pack()

        self.hostNameText.pack()
        self.hostName.pack()

        tk.Label(self.connectTab, text=" ").pack()

        self.connect.pack()

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

        tk.Label(self.connectTab, text=" ").pack()

        self.checkByWalking.pack()

        self.pepperWalk.pack()
        self.roseWalk.pack()
        self.mountainWalk.pack()
        self.cactusWalk.pack()
        self.spiderWalk.pack()

        self.pepperWalk.place(relx=0.4, rely=0.3, anchor="w")
        self.roseWalk.place(relx=0.4, rely=0.4, anchor="w")
        self.mountainWalk.place(relx=0.4, rely=0.5, anchor="w")
        self.cactusWalk.place(relx=0.4, rely=0.6, anchor="w")
        self.spiderWalk.place(relx=0.4, rely=0.7, anchor="w")

    def maxLoadTimeChange(self):
        tm = self.maxLoad.get()

        if str(tm).isnumeric():
            writeFile("guiFiles/maxLoadTime.txt", tm)

        else:
            pyautogui.alert("Make sure to set max load time to a number!")

    def webhookChange(self):
        webhook = self.webhook.get()

        writeFile("guiFiles/webhook.txt", webhook)

    def privateServersChange(self):
        privateServers = []

        for i in range(5):
            privateServer = globals()[f"self.{i + 1}"].get()

            privateServers.append(privateServer)

        writeFile("guiFiles/privateServers.txt", str(privateServers))
        writeFile("guiFiles/joinPrivateServers.txt", True if self.usingPs.get() else False)

    def walkInFieldsChange(self):
        walkInFields = {
            "pepper": self.walkInPepper.get(),
            "rose": self.walkInRose.get(),
            "mountain": self.walkInMountain.get(),
            "cactus": self.walkInCactus.get(),
            "spider": self.walkInSpider.get(),
        }

        writeFile("guiFiles/walk.txt", str(walkInFields))
        writeFile("guiFiles/vicHopping.txt", True if self.vicHopping.get() else False)

    def getPrivateServer(self, n):
        privateServers = eval(readFile("guiFiles/privateServers.txt"))

        return privateServers[n]

    def startMacro(self, main=False):
        self.maxLoadTimeChange()
        self.webhookChange()
        self.privateServersChange()
        self.walkInFieldsChange()

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

            pyautogui.alert(f"Recieved connection from {self.ip} port {self.port}")

            self.AltConnection.recieveNightServers()

        except:
            sendMessage("Alt connection failed...")

            pyautogui.alert("Alt connection failed...")

    def saveSettings(self):
        self.maxLoadTimeChange()
        self.webhookChange()
        self.privateServersChange()
        self.walkInFieldsChange()

        self.window.after(1000, self.saveSettings)
