import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
def calculate_perimeter_triangle(a, b, c):
        return a + b + c