import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))