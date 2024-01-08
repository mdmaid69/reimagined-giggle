import array
def get_array_as_repr(array):
        return repr(array)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()