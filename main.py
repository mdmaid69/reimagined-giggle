import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import math
def calculate_cosine(x):
        return math.cos(x)