import sys
def add_to_python_path(path):
        sys.path.append(path)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()