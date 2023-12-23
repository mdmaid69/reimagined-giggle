import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))