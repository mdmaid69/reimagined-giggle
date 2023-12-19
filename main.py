import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]