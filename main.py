import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import array
def remove_from_array(array, item):
        array.remove(item)