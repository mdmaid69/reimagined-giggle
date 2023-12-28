import array
def get_array_slice(array, i, j):
        return array[i:j]
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()