import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))