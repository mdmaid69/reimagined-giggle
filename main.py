import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))