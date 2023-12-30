import math
def calculate_factorial(n):
        return math.factorial(n)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))