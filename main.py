import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)