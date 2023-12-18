import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)