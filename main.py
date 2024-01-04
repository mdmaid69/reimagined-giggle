import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)