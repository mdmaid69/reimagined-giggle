  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()