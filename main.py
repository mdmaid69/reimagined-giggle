def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()