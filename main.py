import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()