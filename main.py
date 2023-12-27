import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import itertools
print(list(itertools.permutations([1, 2, 3])))