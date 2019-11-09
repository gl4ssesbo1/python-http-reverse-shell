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

## Pandoc compiliation
`pandoc project1.md -o project.pdf --from markdown --template eisvogel --listing --toc`