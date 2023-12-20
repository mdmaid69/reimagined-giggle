import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)