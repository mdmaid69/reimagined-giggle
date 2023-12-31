import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import array
def insert_into_array(array, i, item):
        array.insert(i, item)