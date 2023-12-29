import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()