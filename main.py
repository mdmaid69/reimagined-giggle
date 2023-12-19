import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))