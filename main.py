import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"