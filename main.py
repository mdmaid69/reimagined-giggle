import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)