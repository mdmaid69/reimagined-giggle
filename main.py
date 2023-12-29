import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))