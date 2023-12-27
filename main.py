import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))