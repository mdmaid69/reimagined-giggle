  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()