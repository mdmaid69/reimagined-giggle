import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import array
def set_array_item(array, i, item):
        array[i] = item