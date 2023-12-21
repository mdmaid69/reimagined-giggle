import random
def roll_die():
        return random.randint(1, 6)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()