n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))