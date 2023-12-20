import array
def extend_array(array, iterable):
        array.extend(iterable)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()