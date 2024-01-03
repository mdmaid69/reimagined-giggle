  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()