import socket
from functions import sendMessage, readFile, click, offsetDims, sendScreenshot, writeFile
import time
import threading

class AltConnection:
    def __init__(self, port):
        self.port = port
        self.client = 0

    def connectToAlt(self):
        tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        tcpsocket.bind((socket.gethostname(), self.port))

        sendMessage("Waiting for alt to connect...")

        tcpsocket.listen()

        (client, (ip, port)) = tcpsocket.accept()

        self.client = client

        sendMessage("Alt connected!")

        return ip, port

    def recieveNightServers(self, timeout=20 * 60):
        lastCheck = time.time()

        while True:
            try:
                url = self.client.recv(1024)

                if time.time() - lastCheck >= timeout:
                    raise TimeoutError

                if "roblox" in url:
                    print(f"Url: {url}")

                    lastCheck = time.time()

                url = url.decode()

                writeFile("guiFiles/url.txt", url)

            except Exception:
                print("Lost connection to alt. Closing socket client...")

                sendMessage("Lost connection to alt. Closing socket client...")

                self.client.shutdown(socket.SHUT_RDWR)

                self.client.close()

                time.sleep(5)

                print("Reconnecting to alt...")

                self.connectToAlt()

                t = threading.Thread(target=self.recieveNightServers, args=(timeout,))
                t.daemon = True

                t.start()

                break