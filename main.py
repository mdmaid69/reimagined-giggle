import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()