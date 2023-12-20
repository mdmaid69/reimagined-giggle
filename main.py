def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()