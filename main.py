import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()