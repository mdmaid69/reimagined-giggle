import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()