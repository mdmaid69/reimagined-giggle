  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()