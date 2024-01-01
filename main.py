import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  def calculate_area_triangle(b, h):
        return 0.5 * b * h