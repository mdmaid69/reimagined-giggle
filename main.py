import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)