# EH-Proj1

Ethical Hacking Class Project: HTTP Reverse Shell

This is for educational purposes only!

## Setup

* Install dependencies `pip3 install -r requirements.txt`
  * requests
  * pyinstaller
* Ensure the IP in client.py is correct
* Create an compiled script using pyinstaller
  * pyinstaller --onefile client.py
    * `this will need to be placed onto the victims machine`
    * If you want an exe ensure to run pyinstaller on a windows machine
    * Same goes for ELF or MACH file
* Run server.py
* Wait for victim to run client.py

## Server Commands

The server takes input from the attacker during GET requests and sends the command to the client machine.
The client machine can run any command as long as it is supported by the OS.
    For example if you have placed the compiled client script on a windows machine don't expect ls to work

The client has three special command paths:

* `t` or `terminate`: kill connection to server
* `!`: exports registry keys from client to server
* `^`: exports provided file from client to server
  * Takes one parameter, the path of the file to be exported
    * i.e. `^ /etc/hosts`
  * TODO: allow multiple files to be exported


Sending initial command (tcp.stream eq 2)
    handshake              -> packet no. 184 - 186
    victim sends get       -> packet no. 187
    attacker sends !       -> packet no. 191

Sending file            (tcp.stream eq 7)
    handshake              -> packet no. 759 - 761
    file download start    -> packet no. 762
    file download ends     -> packet no. 36751
    attacker confirms file -> packet no. 36761