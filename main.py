import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)