import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
n = 10
print("Powers of 2:", [2**x for x in range(n)])