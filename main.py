  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()