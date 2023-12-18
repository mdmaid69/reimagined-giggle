import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()