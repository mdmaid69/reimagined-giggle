import collections
def create_user_dict():
        return collections.UserDict()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))