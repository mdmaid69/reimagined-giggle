  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()