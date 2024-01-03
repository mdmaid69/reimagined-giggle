  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()