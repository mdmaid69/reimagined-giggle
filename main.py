import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)