import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))