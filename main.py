import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius