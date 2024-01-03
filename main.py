import array
def get_array_index(array, item):
        return array.index(item)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))