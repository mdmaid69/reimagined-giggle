import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()