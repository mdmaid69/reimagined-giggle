import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)