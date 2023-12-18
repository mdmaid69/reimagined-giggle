def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()