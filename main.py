import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()