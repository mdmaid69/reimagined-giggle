import array
def get_array_typecode(array):
        return array.typecode
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))