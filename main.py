import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)