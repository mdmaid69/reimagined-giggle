import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)