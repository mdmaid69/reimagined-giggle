import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import collections
def count_elements(iterable):
        return collections.Counter(iterable)