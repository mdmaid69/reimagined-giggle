import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()