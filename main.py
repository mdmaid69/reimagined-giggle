import glob
def find_files(pattern):
        return glob.glob(pattern)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()