import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()