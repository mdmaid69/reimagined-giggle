  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()