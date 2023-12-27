import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()