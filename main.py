import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
n = 10
print("Square numbers:", [x**2 for x in range(n)])