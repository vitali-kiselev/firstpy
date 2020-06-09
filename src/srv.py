import os
import socketserver #импортируем стандартную библиотеку для работы с сервером
from http.server import SimpleHTTPRequestHandler
from urllib.parse import parse_qs

PORT = int(os.getenv("PORT", 8000))
print(f"PORT = {PORT}")

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/hello"):
            return self.handle_hallo()
        else:
            return SimpleHTTPRequestHandler(self)
    def handle_hallo(self):
        args = self.build_query_args()
        name = args.get("name", "anonim")
        msg = f"Hello {name}"
        self.respond(msg)
    def build_query_args(self):
        path, *qs = self.path.split("?")
        args = {}
        if len(qs) != 1:
            return args
            qs = parse_qs(qs)
            name = qs["name"][0]

    def respond(self,msg: str):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", str(len(msg)))
        self.end_headers()


            

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("it" + " works")
    httpd.serve_forever()