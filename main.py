import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)