import itertools
print(list(itertools.permutations([1, 2, 3])))
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()