import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)