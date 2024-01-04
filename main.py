import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))