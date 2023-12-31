import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))