def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()