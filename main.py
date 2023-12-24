import array
def get_array_as_int(array):
        return int(array[0])
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))