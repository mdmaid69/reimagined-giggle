def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()