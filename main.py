import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
text = "Hello, world!"
print("Uppercase:", text.upper())