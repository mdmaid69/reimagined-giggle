import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))