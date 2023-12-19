import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
n = 10
print("Square numbers:", [x**2 for x in range(n)])