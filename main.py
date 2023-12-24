import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)