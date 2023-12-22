import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])