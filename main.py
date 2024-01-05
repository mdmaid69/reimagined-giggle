import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import math
def calculate_logarithm_base_2(x):
        return math.log2(x)