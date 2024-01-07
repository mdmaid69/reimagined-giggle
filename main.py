import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()