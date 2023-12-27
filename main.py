import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()