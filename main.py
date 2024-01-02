import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable