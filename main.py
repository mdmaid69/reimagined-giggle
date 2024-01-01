import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)