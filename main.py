import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))