import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))