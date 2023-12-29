import array
def get_array_as_frozenset(array):
        return frozenset(array)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()