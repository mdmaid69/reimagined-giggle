def calculate_area(radius):
        return 3.14 * radius * radius
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()