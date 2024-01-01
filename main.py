import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()