  def calculate_area_rectangle(l, w):
        return l * w
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()