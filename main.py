  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()