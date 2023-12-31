import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)