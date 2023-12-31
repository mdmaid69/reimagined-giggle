import math
def calculate_tangent(x):
        return math.tan(x)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))