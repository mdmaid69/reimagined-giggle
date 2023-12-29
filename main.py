import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()