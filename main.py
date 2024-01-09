import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import json
print(json.dumps({"name": "John", "age": 30}))