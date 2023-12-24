import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()