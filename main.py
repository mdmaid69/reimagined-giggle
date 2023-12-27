import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets