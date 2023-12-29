import random
def generate_random_choice(choices):
        return random.choice(choices)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))