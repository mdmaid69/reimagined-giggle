import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()