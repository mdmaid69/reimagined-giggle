import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()