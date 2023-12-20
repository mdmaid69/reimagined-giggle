import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)