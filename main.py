import datetime
def get_current_datetime():
        return datetime.datetime.now()
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()