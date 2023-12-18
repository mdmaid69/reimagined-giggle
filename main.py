import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)