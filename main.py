import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"