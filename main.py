import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)