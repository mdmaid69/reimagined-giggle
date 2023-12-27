import math
def calculate_factorial(n):
        return math.factorial(n)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()