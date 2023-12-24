import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))