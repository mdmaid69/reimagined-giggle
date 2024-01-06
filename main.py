import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)