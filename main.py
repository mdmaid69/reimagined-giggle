n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))