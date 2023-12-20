import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"