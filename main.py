import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)