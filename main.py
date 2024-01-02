import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
n = 10
print("Powers of 2:", [2**x for x in range(n)])