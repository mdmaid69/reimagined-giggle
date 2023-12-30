  def calculate_area_circle(r):
        return 3.14 * r**2
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()