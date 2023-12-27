import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()