def calculate_force(mass, acceleration):
        return mass * acceleration
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))