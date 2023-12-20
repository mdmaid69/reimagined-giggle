import json
def convert_to_json(data):
        return json.dumps(data)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))