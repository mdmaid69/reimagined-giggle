def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()