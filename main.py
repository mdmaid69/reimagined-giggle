  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()