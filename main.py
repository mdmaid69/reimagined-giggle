  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()