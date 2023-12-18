import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))