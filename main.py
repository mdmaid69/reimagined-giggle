import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()