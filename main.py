n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()