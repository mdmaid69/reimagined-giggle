import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)