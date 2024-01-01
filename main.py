import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()