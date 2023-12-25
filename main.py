import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()