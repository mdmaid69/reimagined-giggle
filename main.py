n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()