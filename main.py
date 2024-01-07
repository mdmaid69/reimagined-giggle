import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b