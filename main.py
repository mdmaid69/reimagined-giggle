import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))