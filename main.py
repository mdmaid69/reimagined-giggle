import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import array
def pop_from_array(array, i=-1):
        return array.pop(i)