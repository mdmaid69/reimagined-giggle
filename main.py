import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets