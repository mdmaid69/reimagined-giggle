import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)