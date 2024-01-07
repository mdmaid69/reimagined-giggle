import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()