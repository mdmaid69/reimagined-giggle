import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()