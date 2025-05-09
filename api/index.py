from http.server import BaseHTTPRequestHandler
from ddos import send_request

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        result = send_request()  # вызов функции из test1.py
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return