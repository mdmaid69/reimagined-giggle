  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()