import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))