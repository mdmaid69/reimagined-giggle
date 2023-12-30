import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()