import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()