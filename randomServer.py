import requests
import random
import webbrowser
import time

from functions import readFile

lastRequest = 0

servers_data = ""

psN = 0
psTime = 0

def joinRandomServer(place_id = 1537690962):
    global lastRequest
    global servers_data
    global psN
    global psTime

    join = False

    if bool(readFile("guiFiles/joinPrivateServers.txt")):
        if time.time() - psTime >= 3:
            try:
                print(f"Joining private server {psN + 1}")

                join_url = eval(readFile("guiFiles/privateServers.txt"))[psN]
                join_url = join_url.split("code=")[1]

                webbrowser.open("roblox://placeID=1537690962&linkcode=" + join_url)

                if psN >= 5:
                    psN = 1

                    psTime = time.time()

                else:
                    psN += 1

                return join_url

            except:
                if psN >= 5:
                    psN = 1

                    psTime = time.time()

                else:
                    psN += 1

                url = joinRandomServer(place_id)

                return url

    print("Joining public server")

    if time.time() - lastRequest >= 30:
        # URL for Roblox game instances (servers)
        api_url = f'https://games.roblox.com/v1/games/{place_id}/servers/Public?sortOrder=Asc&limit=100'

        # Fetch the list of active servers
        response = requests.get(api_url)
        newServers_data = response.json()

        if 'data' in newServers_data and len(newServers_data['data']) > 0:
            servers_data = newServers_data

    try:
        if 'data' in servers_data and len(servers_data['data']) > 0:
            join = True

        else:
            time.sleep(10)

            url = joinRandomServer(place_id)

            return url

    except:
        pass

    if join:
        servers = servers_data['data']

        # Choose a random server
        random_server = random.choice(servers)
        server_id = random_server['id']

        # Generate the Roblox server join link
        join_url = f'roblox://placeID={place_id}&gameInstanceId={server_id}'

        # Open the Roblox client to join the server
        webbrowser.open(join_url)

        return join_url
