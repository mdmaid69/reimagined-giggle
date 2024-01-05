import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import math
def calculate_absolute_value(x):
        return math.fabs(x)