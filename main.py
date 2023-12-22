import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import json
def read_from_json(json_string):
        return json.loads(json_string)