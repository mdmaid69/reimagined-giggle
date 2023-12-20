import array
def convert_array_to_unicode(array):
        return array.tounicode()
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()