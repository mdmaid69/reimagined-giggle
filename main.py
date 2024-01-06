import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity