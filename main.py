import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()