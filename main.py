import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)