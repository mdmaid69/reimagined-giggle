import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))