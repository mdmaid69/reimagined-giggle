import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)