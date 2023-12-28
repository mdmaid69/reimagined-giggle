import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()