import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)