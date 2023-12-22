import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)