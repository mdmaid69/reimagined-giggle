text = "Hello, world!"
print("Reversed:", text[::-1])
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()