import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()