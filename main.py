import math
def calculate_arc_cosine(x):
        return math.acos(x)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()