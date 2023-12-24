import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time