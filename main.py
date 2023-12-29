import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)