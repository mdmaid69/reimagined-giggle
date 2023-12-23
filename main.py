def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))