import math
def calculate_sign(x):
        return math.copysign(1, x)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))