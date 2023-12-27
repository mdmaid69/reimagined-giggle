import array
def check_if_array_contains_item(array, item):
        return item in array
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()