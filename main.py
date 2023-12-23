import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))