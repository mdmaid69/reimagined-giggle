import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)