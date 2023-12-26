  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()