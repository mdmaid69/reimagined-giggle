import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height