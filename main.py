import array
def get_array_as_complex(array):
        return complex(array[0])
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()