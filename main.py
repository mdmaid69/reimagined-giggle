import array
def get_array_as_frozenset(array):
        return frozenset(array)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))