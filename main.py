import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)