  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()