import array
def get_array_itemsize(array):
        return array.itemsize
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()