import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)