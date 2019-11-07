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

## PCAP Analysis

Downloading File	(tcp.stream eq 21)
	handshake			-> packet no. 616 - 618
	http get exploit		-> packet no. 619
	download starts			-> packet no. 621
	download ends			-> packet no. 1166
	http ok				-> packet no. 1167

Sending initial command (tcp.stream eq 26)
	handshake			-> packet no. 1612 - 1614
	http get command from server	-> packet no. 1615
	http ok /w command		-> packet no. 1618

Sending file            (tcp.stream eq 31)
	handshake			-> packet no. 2001 - 2003
	reg zip  download starts	-> packet no. 2004
	reg zip  download ends		-> packet no. 25669
	http post to send file		-> packet no. 25662
	http ok ack file transfer	-> packet no. 25673
