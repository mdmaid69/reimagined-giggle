import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()