import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()