import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))