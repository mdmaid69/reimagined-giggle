import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))