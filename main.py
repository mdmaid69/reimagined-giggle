import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)