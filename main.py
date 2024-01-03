import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)