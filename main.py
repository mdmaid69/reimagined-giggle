import random
def generate_random_choice(choices):
        return random.choice(choices)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()