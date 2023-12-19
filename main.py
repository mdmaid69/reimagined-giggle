import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()