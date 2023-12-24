n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()