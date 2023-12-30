import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))