import array
def get_array_as_tuple(array):
        return tuple(array)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))