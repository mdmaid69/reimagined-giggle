import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import random
def generate_random_number(start, end):
        return random.randint(start, end)