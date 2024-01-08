  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()