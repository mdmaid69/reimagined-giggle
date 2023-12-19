i = 0
while i < 5:
        print(i)
        i += 1
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))