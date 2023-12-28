import os
def list_files_in_directory(path):
        return os.listdir(path)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()