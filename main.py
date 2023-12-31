def calculate_volume(length, width, height):
        return length * width * height
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))