import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))