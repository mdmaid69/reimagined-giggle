import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)