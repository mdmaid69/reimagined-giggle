import array
def get_array_as_bytearray(array):
        return bytearray(array)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()