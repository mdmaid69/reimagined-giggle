def calculate_roi(gain, cost):
        return (gain - cost) / cost
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()