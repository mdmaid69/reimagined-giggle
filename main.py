import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)