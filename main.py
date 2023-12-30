def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()