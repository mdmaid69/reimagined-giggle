import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()