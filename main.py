import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()