numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()