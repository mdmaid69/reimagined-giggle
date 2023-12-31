import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)