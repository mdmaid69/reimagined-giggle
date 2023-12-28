import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()