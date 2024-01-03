import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()