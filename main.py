import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()