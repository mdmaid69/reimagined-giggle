import collections
def create_ordered_dict():
        return collections.OrderedDict()
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()