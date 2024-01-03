import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()