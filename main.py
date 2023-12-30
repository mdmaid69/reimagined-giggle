def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()