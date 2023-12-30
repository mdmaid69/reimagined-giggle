import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))