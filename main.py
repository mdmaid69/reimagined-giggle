import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities