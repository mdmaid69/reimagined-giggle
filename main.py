import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))